import json
from models import DriverCreate

def save_drivers(drivers):
    with open("data/drivers.json", "w") as file:
        json.dump(drivers, file)


def load_drivers():
    with open("data/drivers.json", "r") as file:
        drivers = json.load(file)

    return drivers


def get_all_drivers():
    return load_drivers()


def get_driver_by_id(driver_id: int):
    drivers = load_drivers()

    for driver in drivers:
        if driver["id"] == driver_id:
            return driver

    return None


def create_driver(driver: DriverCreate):
    drivers = load_drivers()
    if drivers:
        new_id = max(drivers, key=lambda x: x["id"]) ["id"] + 1
    else:
        new_id = 1
    
    new_driver = {
        "id": new_id,
        "name": driver.name,
        "team": driver.team,
        "points": driver.points
        }
    
    drivers.append(new_driver)
    save_drivers(drivers)
    
    return new_driver


def update_driver(driver:DriverCreate, driver_id: int):
    drivers = load_drivers()
    for piloto in drivers:
        if piloto["id"] == driver_id:
            piloto["name"] = driver.name
            piloto["team"] = driver.team
            piloto["points"] = driver.points
                
            save_drivers(drivers)
            return piloto
    return None


def delete_driver(driver_id: int):
    drivers = load_drivers()
    for piloto in drivers:
        if piloto["id"] == driver_id:
            drivers.remove(piloto)
    
            save_drivers(drivers)
            return piloto
    return None


def get_driver_ranking(limit:int):
    drivers = get_all_drivers()
    ranking = sorted(drivers, key=lambda driver: driver["points"], reverse=True)
    ranking_with_position = [
        {**driver, "position": index} for index, driver in enumerate(ranking, start=1)
    ]
    return ranking_with_position[:limit]

def get_driver_statistics():
    drivers = load_drivers()
    if not drivers:
        return None
    points = [driver["points"] for driver in drivers]
    drivers_statistics = {
        "total_drivers" : len(drivers),
        "total_points": sum(points),
        "average_points": sum(points)/len(points),
        "highest_points": max(points),
        "lowest_points": min(points)
    }

    return drivers_statistics

def get_team_statistics():
    drivers = load_drivers()
    if not drivers:
        return None
    team_statistics = {}

    for driver in drivers:
        if driver["team"] in team_statistics:
            team_statistics[driver["team"]]["drivers"] += 1
            team_statistics[driver["team"]]["points"] += driver["points"]
        else:

            team_statistics[driver["team"]] = {
                "drivers": 1,
                "points": driver["points"]
            } 

    return team_statistics