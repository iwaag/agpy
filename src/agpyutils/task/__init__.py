from agpyutils.task.hatchet.hub import TaskHub_Hatchet
from agpyutils.task.hub import TaskHub

hub = TaskHub_Hatchet()
def get_task_hub() -> TaskHub:
    return hub