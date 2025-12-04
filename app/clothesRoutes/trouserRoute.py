from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from ..models import *
from ..config import trousers_db

trouserRouter = APIRouter()

@trouserRouter.get("/trouser/get")
async def get_all_trousers():
    try:
        data = list(trousers_db.find())
        return all_shirts(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching shirts: {e}")

@trouserRouter.post("/trouser/create")
async def create_trouser(new_trouser: TrouserClass):
    try:
        resp = trousers_db.insert_one(dict(new_trouser))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


@trouserRouter.get("/trouser/geto/{id}")
async def get_trouser_id(id: int):
    try:
        data = list(trousers_db.find())
        resp = return_value2(data,id)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")