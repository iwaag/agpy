from pydantic import BaseModel


class BaseResourceRef(BaseModel):
    domain: str
    user_id: str | None = None
    project_id: str | None = None

class StaticObjectRef(BaseResourceRef):
    relative_key: str

class NewDynamicObjectGroupRequest(BaseResourceRef):
    caetegory: str

class DynamicObjectRef(BaseResourceRef):
    group_id: str
    relative_key: str

class PresignUploadOption(BaseModel):
    expires_in: int = 3600
    content_type: str | None = None

class PresignDownloadOption(BaseModel):
    expires_in: int = 3600
    response_content_type: str | None = None
    response_content_disposition: str | None = None

class CopyObjectRequest(BaseModel):
    source_strage_resource_id: str
    destination_strage_resource_id: str