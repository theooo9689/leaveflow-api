from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.config import Settings, get_settings

router = APIRouter(prefix="/system", tags=["System"])


class SystemInfoResponse(BaseModel):
    name: str
    version: str
    environment: str


@router.get(
    "/info",
    response_model=SystemInfoResponse,
    summary="Get public API information",
)
def get_system_info(
    settings: Annotated[Settings, Depends(get_settings)],
) -> SystemInfoResponse:
    return SystemInfoResponse(
        name=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )
