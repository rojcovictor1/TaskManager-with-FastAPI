from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from ..schemas.task import TaskCreate, TaskResponse
from ...core.security import get_current_user
from ...db.dependencies import get_db
from ...db.models import Task, User

router = APIRouter()


@router.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    # Creating a new task with the title, description, user ID from the authenticated user,
    # default completion status as False, and timestamp of creation.
    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=current_user.id,  # Using user_id from the authenticated user
        is_completed=False,
        created_at=datetime.utcnow()
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/tasks/", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
    # Fetching all tasks created by the authenticated user using their user ID.
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)):
    # Retrieving a specific task by task ID and user ID to ensure it belongs to the
    # authenticated user.
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    # Updating a task identified by task ID for the authenticated user. Only title and
    # description are updatable.
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = task_update.title
    task.description = task_update.description
    db.commit()
    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    # Deleting a task by task ID, verifying that it belongs to the authenticated user before
    # deletion.
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}
