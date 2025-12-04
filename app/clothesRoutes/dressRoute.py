from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from ..models import *
from ..config import dress_db

dressRouter = APIRouter()

@dressRouter.get("/dress/get")
async def get_all_dresses():
    try:
        data = list(dress_db.find())
        return all_dresses(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching shirts: {e}")

@dressRouter.post("/dress/create")
async def create_dress(new_dress: DressClass):
    try:
        resp = dress_db.insert_one(dict(new_dress))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


@dressRouter.get("/dress/geto/{id}")
async def get_dress_id(id: int):
    try:
        data = list(dresses_db.find())
        resp = return_value2(data,id)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")