import httpx
import os
from agpy.contracts.storage import (
    StaticObjectRef,
    PresignDownloadOption,
    PresignUploadOption
)

STORAGE_SERVICE_URL=os.getenv("STORAGE_SERVICE_URL")
STATIC_DOWNLOAD_PRESIGN_URL=f"{STORAGE_SERVICE_URL}/static_object/download"
STATIC_UPLOAD_PRESIGN_URL=f"{STORAGE_SERVICE_URL}/static_object/upload"
DYNAMIC_DOWNLOAD_PRESIGN_URL=f"{STORAGE_SERVICE_URL}/dynamic_object/download"
DYNAMIC_UPLOAD_PRESIGN_URL=f"{STORAGE_SERVICE_URL}/dynamic_object/upload"

async def get_static_object_download_url(
    auth_header: str,
    object_ref: StaticObjectRef,
    option: PresignDownloadOption = PresignDownloadOption()
) -> str:
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.post(
            STATIC_DOWNLOAD_PRESIGN_URL,
            headers={"authorization": auth_header},
            json={"ref": object_ref.model_dump(), "option": option.model_dump()}
        )
        return response.text

async def get_static_object_upload_url(
    auth_header: str,
    object_ref: StaticObjectRef, 
    option: PresignUploadOption = PresignUploadOption()
) -> str:
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.post(
            STATIC_UPLOAD_PRESIGN_URL,
            headers={"authorization": auth_header},
            json={"ref": object_ref.model_dump(), "option": option.model_dump()}
        )
        return response.text