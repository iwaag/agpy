from hatchet_sdk import DurableContext, hatchet, Context
from datetime import timedelta

from agpyutils.task.models import Task_UnmanagedLabor

@hatchet.durable_task(name="labor", input_validator=Task_UnmanagedLabor)
async def task_unmanaged_labor(input: Task_UnmanagedLabor, context: DurableContext) -> dict[str, str]:
    try:
        revent = context.aio_sleep_for(input.wait_for)
        return {"status": "success",}
    except Exception as e:
        print(e)
        return {"status": "failed",}