from typing import Annotated, Optional
from fastapi import FastAPI, Depends  # type: ignore
from pydantic import BaseModel  # type: ignore


app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(BaseModel):
    id: int


task = []


@app.post("/task")
async def add_task(
    task: Annotated[STaskAdd, Depends()]  # type: ignore
):
    task.append(task)
    return {"ok": True}

# @app.get("/task")
# def get_task():
# task = Task(name="Write down this video")
# return {"data": task}
