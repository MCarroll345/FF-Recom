from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from ..models import *
from ..config import skirt_db

skirtRouter = APIRouter()

@skirtRouter.get("/skirt/get")
async def get_all_skirts():
    try:
        data = list(skirt_db.find())
        return all_skirts(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching shirts: {e}")

@skirtRouter.post("/skirt/create")
async def create_skirt(new_skirt: SkirtClass):
    try:
        resp = skirt_db.insert_one(dict(new_skirt))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


@skirtRouter.get("/skirt/geto/{id}")
async def get_skirt_id(id: int):
    try:
        data = list(skirt_db.find())
        resp = return_value2(data,id)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")