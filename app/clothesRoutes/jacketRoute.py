from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from ..models import *
from ..config import jacket_db

jacketRouter = APIRouter()

@jacketRouter.get("/jacket/get")
async def get_all_jackets():
    try:
        data = list(jacket_db.find())
        return all_jackets(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching shirts: {e}")

@jacketRouter.post("/jacket/create")
async def create_jacket(new_jacket: JacketClass):
    try:
        resp = jacket_db.insert_one(dict(new_jacket))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


@jacketRouter.get("/jacket/geto/{id}")
async def get_jacket_id(id: int):
    try:
        data = list(jacket_db.find())
        resp = return_value2(data,id)
        return resp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")