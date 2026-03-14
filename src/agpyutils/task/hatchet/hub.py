from abc import abstractmethod

from agpyutils.task.hub import TaskHub
import agpyutils.task.models as models
import agpyutils.task.hatchet.workflows.basic as workflows_basic
from hatchet_sdk import Hatchet
import asyncio

hatchet = Hatchet()
try:
    worker = hatchet.worker("test-connection")
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")

class TaskHub_Hatchet(TaskHub):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def request_unmanaged_labor(self, task: models.Task_UnmanagedLabor):
        aiotask = workflows_basic.task_unmanaged_labor(input=task)
        asyncio.run(aiotask)

