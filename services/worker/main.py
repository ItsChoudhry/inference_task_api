from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import time
import httpx

app = FastAPI()


class ProcessPayload(BaseModel):
    task_id: str
    model: str
    inputs: dict


@app.post("/process")
def process_task(
    payload: ProcessPayload,
    x_worker_key: str = Header(...),
):
    if x_worker_key != "worker-key":
        raise HTTPException(403)

    httpx.post(
        "http://api:8000/internal/update-status",
        json={
            "task_id": payload.task_id,
            "status": "processing",
            "result_url": f"https://results.example.com/{payload.task_id}.json",
        },
        headers={"X-Internal-Key": "internal-key"},
    )

    #  work xd
    time.sleep(30)

    httpx.post(
        "http://api:8000/internal/update-status",
        json={
            "task_id": payload.task_id,
            "status": "completed",
            "result_url": f"https://results.example.com/{payload.task_id}.json",
        },
        headers={"X-Internal-Key": "internal-key"},
    )

    return {"status": "processed"}
