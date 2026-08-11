from fastapi import FastAPI, HTTPException

import json

app = FastAPI()

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