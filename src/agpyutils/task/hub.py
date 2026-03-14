from abc import ABC, abstractmethod

from agpyutils.task.models import Task_UnmanagedLabor
from agpyutils.task.hatchet.hub import TaskHub_Hatchet

class TaskHub(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def request_unmanaged_labor(self, task: Task_UnmanagedLabor):
        pass

hub = TaskHub_Hatchet()
def get_task_hub() -> TaskHub_Hatchet:
    return hub