from fastapi import FastAPI
from routers.drivers import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "F1 Data Analyzer API"}
