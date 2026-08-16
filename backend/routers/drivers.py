from fastapi import APIRouter
from services import get_all_drivers

router = APIRouter()

@router.get("/drivers")
def lista_pilotos():
    return get_all_drivers()