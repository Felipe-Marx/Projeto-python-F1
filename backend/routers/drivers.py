from fastapi import APIRouter, HTTPException, Query
from models import DriverCreate
from services import (
    get_all_drivers, 
    get_driver_by_id,
    create_driver as create_driver_service, 
    update_driver as update_driver_service, 
    delete_driver as delete_driver_service,
    get_driver_ranking, get_driver_statistics
    )

router = APIRouter()

@router.get("/drivers")
def lista_pilotos():
    return get_all_drivers()


@router.get("/drivers/ranking")
def drivers_ranking(limit:int = Query(5, ge=1, le=22)):
    return get_driver_ranking(limit)


@router.get("/drivers/statistics")
def get_drivers_statistics():
    result = get_driver_statistics()
    if result is None:
        raise HTTPException(status_code=404, detail="Drivers not found")

    return result


@router.get("/drivers/{driver_id}")
def get_driver(driver_id: int):
    result = get_driver_by_id(driver_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return result


@router.post("/drivers")
def create_driver(driver: DriverCreate):
    return create_driver_service(driver)


@router.put("/drivers/{driver_id}")
def update_driver(driver:DriverCreate, driver_id: int):
    result = update_driver_service(driver, driver_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return result


@router.delete("/drivers/{driver_id}")
def delete_driver(driver_id: int):
    result = delete_driver_service(driver_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return result

