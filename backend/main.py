from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

app = FastAPI()

class DriverCreate(BaseModel):
    name: str
    team: str
    points: int

@app.get("/")
def home():
    return {"message": "F1 Data Analyzer API"}

def load_drivers():
    with open("data/drivers.json", "r") as file:
        drivers = json.load(file)

    return drivers

@app.get("/drivers")
def lista_pilotos():
    return load_drivers()

@app.get("/drivers/{driver_id}")
def get_driver(driver_id: int):
    drivers = load_drivers()

    for driver in drivers:
        if driver["id"] == driver_id:
            return driver
        
    raise HTTPException(status_code=404, detail="Driver not found")

@app.post("/drivers")
def create_driver(driver:DriverCreate):
    drivers = load_drivers()
    new_id = max(drivers, key=lambda x: x["id"]) ["id"] + 1

    new_driver = {
        "id": new_id,
        "name": driver.name,
        "team": driver.team,
        "points": driver.points
    }

    drivers.append(new_driver)
    with open("data/drivers.json", "w") as file:
        json.dump(drivers, file)

    return new_driver