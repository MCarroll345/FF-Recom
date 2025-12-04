from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from ..models import *
from ..config import shoes_db

shoeRouter = APIRouter()

@shoeRouter.get("/shoe/get")
async def get_all_shoes():
    try:
        data = list(shoes_db.find())
        return all_shoes(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching shirts: {e}")

@shoeRouter.post("/shoes/create")
async def create_shoes(new_shoes: ShoeClass):
    try:
        resp = shoes_db.insert_one(dict(new_shoes))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


@shoeRouter.get("/shoes/geto/{id}")
async def get_shoes_id(id: int):
    try:
        data = list(shoes_db.find())
        resp = return_value2(data,id)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")