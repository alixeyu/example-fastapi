from fastapi import APIRouter

router = APIRouter(tags=['home'])


@router.get('/')
def read_root():
    return {'details': 'Home page'}
