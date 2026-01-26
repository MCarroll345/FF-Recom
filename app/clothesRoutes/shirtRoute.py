from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from ..models import *
from ..config import db

shirtRouter = APIRouter()

@shirtRouter.get("/{cloth}/get")
async def get_all(cloth: str):
    try:
        data = list(db[cloth].find())
        return all_items(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching {cloth}: {e}")

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