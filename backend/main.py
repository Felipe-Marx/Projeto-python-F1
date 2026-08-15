from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

class DriverCreate(BaseModel):
    name: str = Field(min_length=1)
    team: str = Field(min_length=1)
    points: int = Field(ge=0)

    @field_validator("name", "team")
    @classmethod
    def verificar_texto(cls, texto:str):
        if not texto.strip():
            raise ValueError("Nome ou Time inválido.")
        return texto.strip()
        
    

def save_drivers(drivers):
    with open("data/drivers.json", "w") as file:
        json.dump(drivers, file)

def load_drivers():
    with open("data/drivers.json", "r") as file:
        drivers = json.load(file)

    return drivers


@app.get("/")
def home():
    return {"message": "F1 Data Analyzer API"}


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
    save_drivers(drivers)

    return new_driver


@app.put("/drivers/{driver_id}")
def update_driver(driver:DriverCreate, driver_id: int):
    drivers = load_drivers()
    for piloto in drivers:
        if piloto["id"] == driver_id:
            piloto["name"] = driver.name
            piloto["team"] = driver.team
            piloto["points"] = driver.points
            
            save_drivers(drivers)
            return piloto
    
    raise HTTPException(status_code=404, detail="Driver not found")


@app.delete("/drivers/{driver_id}")
def delete_driver(driver_id: int):
    drivers = load_drivers()
    for piloto in drivers:
        if piloto["id"] == driver_id:
            drivers.remove(piloto)

            save_drivers(drivers)
            return piloto

    raise HTTPException(status_code=404, detail="Driver not found")

