import time
from typing import Optional

import httpx

from agpy.clients.auth.config import JWKS_CACHE_SECONDS, OIDC_JWKS_URL, require_config


_jwks_cache: Optional[dict] = None
_jwks_cache_expires_at = 0.0


async def fetch_jwks(timeout_seconds: float = 5.0) -> dict:
    jwks_url = require_config(OIDC_JWKS_URL, "OIDC_JWKS_URL")
    async with httpx.AsyncClient(timeout=timeout_seconds) as client:
        response = await client.get(jwks_url)
        response.raise_for_status()
        return response.json()


async def get_jwks() -> dict:
    global _jwks_cache, _jwks_cache_expires_at
    now = time.time()
    if _jwks_cache and now < _jwks_cache_expires_at:
        return _jwks_cache

    jwks = await fetch_jwks()
    _jwks_cache = jwks
    _jwks_cache_expires_at = now + JWKS_CACHE_SECONDS
    return jwks
