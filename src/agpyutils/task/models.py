from datetime import datetime, timedelta
from enum import StrEnum
from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class TaskStatus(StrEnum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

class TaskMetadata(BaseModel):
    task_id: str
    user_id: str
    project_id: str
    status: TaskStatus = TaskStatus.TODO
    priority: int = Field(default=1, ge=1, le=3)
    expire_at: Optional[datetime] = None

class TaskBase(BaseModel):
    meta: TaskMetadata

class Task_UnmanagedLabor(TaskBase):
    redirect_url: HttpUrl
    wait_for: timedelta = timedelta(minutes=5)

class Task_UpdageState(TaskBase):
    auth_url: HttpUrl