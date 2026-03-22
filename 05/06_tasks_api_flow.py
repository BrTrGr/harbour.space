"""Problem 06: POST -> GET tasks flow.

Task:
1. Keep in-memory task storage (dict or list)
2. Implement POST /tasks to add task with generated id
3. Implement GET /tasks to return all tasks
4. Verify: after POST, GET returns added task

Optional:
- Add GET /tasks/{task_id} with 404 for missing task
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class TaskIn(BaseModel):
    title: str
    description: str | None = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None = None


tasks_db: dict[int, TaskOut] = {}
next_id: int = 1


@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskIn) -> TaskOut:
    global next_id
    task = TaskOut(
        id=next_id,
        title=payload.title,
        description=payload.description
    )
    tasks_db[next_id] = task
    next_id += 1
    return task


@app.get("/tasks", response_model=list[TaskOut])
def get_tasks() -> list[TaskOut]:
    return list(tasks_db.values())
