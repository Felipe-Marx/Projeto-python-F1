from fastapi import FastAPI, HTTPException
from routers.drivers import router
from models import DriverCreate
from services import (
    get_driver_by_id,
    create_driver as create_driver_service,
    update_driver as update_driver_service,
    delete_driver as delete_driver_service
)


app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "F1 Data Analyzer API"}


@app.get("/drivers/{driver_id}")
def get_driver(driver_id: int):
    result = get_driver_by_id(driver_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return result


@app.post("/drivers")
def create_driver(driver: DriverCreate):
    return create_driver_service(driver)


@app.put("/drivers/{driver_id}")
def update_driver(driver:DriverCreate, driver_id: int):
    result = update_driver_service(driver, driver_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return result

@app.delete("/drivers/{driver_id}")
def delete_driver(driver_id: int):
    result = delete_driver_service(driver_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return result

