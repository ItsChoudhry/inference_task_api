from .models.task import Task
from .models.task_status import TaskStatus


def mark_pending(task: Task):
    task.update_status(TaskStatus.PENDING)


def mark_processing(task: Task):
    task.update_status(TaskStatus.PROCESSING)


def mark_completed(task: Task, result_url: str):
    task.update_status(TaskStatus.COMPLETED, result_url=result_url)


def mark_failed(task: Task, error: str):
    task.update_status(TaskStatus.FAILED, error=error)
