from agpy.contracts.agcore.mission import (
    MissionInfo,
    MissionStartRequest
)

from agpy.clients.auth.jwt import AuthInfo

async def start_mission(request: MissionStartRequest, AuthInfo: AuthInfo) -> MissionInfo:
    pass