from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from .models import *
from .config import shirts_db

app = FastAPI()
router = APIRouter()

@router.get("/shirts")
async def get_all_shirts():
    try:
        data = list(shirts_db.find())
        return all_shirts(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching shirts: {e}")

@router.post("/shirts")
async def create_user(new_shirt: ShirtClass):
    try:
        resp = shirts_db.insert_one(dict(new_shirt))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


@router.get("/shirts/{id}")
async def get_shirt_id(id: int):
    try:
        data = list(shirts_db.find())
        resp = return_value2(data,id)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")

app.include_router(router)