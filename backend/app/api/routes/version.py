from fastapi import APIRouter
from pydantic import BaseModel

from app.__version__ import version

router = APIRouter()


class Version(BaseModel):
    version: str


@router.get("/version", response_model=Version)
def get_version():
    return Version(version=version)
