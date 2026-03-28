import os

from agpy.contracts.auth.jwt import JWTAuthError


CLIENT_ID = os.getenv("CLIENT_ID")
OIDC_CLIENT_SECRET = os.getenv("OIDC_CLIENT_SECRET")
OIDC_TOKEN_ENDPOINT = os.getenv("OIDC_TOKEN_ENDPOINT")
OIDC_JWKS_URL = os.getenv("OIDC_JWKS_URL")
OIDC_ISSUER = os.getenv("OIDC_ISSUER")
OIDC_AUDIENCE = os.getenv("OIDC_AUDIENCE", "").strip()
JWKS_CACHE_SECONDS = int(os.getenv("JWKS_CACHE_SECONDS", "300"))


def require_config(value: str | None, name: str) -> str:
    if not value:
        raise JWTAuthError(f"{name} is not configured")
    return value
