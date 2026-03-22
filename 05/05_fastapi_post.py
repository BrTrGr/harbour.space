"""Problem 05: add POST handler to FastAPI app.

Task:
1. Keep GET / endpoint
2. Add POST /tasks endpoint
3. Validate body with Pydantic model:
   - title: str
   - completed: bool = False
4. Return created object

Test options:
- Swagger UI: http://127.0.0.1:8000/docs
- curl or requests
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

tasks = {}
next_id = 1

class TaskIn(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok", "message": "FastAPI running"}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskIn) -> dict:
    global next_id
    task = {"id":next_id, **payload.model_dump()}
    tasks[next_id] = task
    next_id += 1
    return task
