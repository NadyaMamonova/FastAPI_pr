from typing import Annotated
from fastapi import APIRouter, Depends

from repozitory import TaskRepozitory
from schemas import STaskAdd, STask, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=['Tаски'],
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepozitory.add_one(task)
    return{"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepozitory.find_all()
    return tasks

