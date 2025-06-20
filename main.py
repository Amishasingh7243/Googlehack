from fastapi import FastAPI, Request
from pydantic import BaseModel
from task_parser import parse_task
from orchestrator import orchestrate_task

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/api/execute")
async def execute_task(req: TaskRequest):
    parsed = parse_task(req.task)
    result = orchestrate_task(parsed)
    return {"status": "executed", "result": result}
