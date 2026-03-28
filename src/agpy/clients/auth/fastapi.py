from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from agpy.clients.auth.jwt import auth_info_from_bearer_token
from agpy.contracts.auth.jwt import AuthInfo


bearer_scheme = HTTPBearer(auto_error=True)


async def get_auth_info(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> AuthInfo:
    return await auth_info_from_bearer_token(credentials.credentials)
