from typing import Dict

from fastapi import APIRouter

router = APIRouter(tags=["home"])


@router.get("/")
def read_root() -> Dict[str, str]:
    return {"details": "Home page"}
