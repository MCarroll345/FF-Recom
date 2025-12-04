from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from ..models import *
from ..config import shirts_db

shirtRouter = APIRouter()

@shirtRouter.get("/shirts/get")
async def get_all_shirts():
    try:
        data = list(shirts_db.find())
        return all_shirts(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching shirts: {e}")

@shirtRouter.post("/shirts/create")
async def create_shirt(new_shirt: ShirtClass):
    try:
        resp = shirts_db.insert_one(dict(new_shirt))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


@shirtRouter.get("/shirts/geto/{id}")
async def get_shirt_id(id: int):
    try:
        data = list(shirts_db.find())
        resp = return_value2(data,id)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")