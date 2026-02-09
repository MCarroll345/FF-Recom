from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from bson import ObjectId
from .models import *
from .config import db

recomRouter = APIRouter()

#Function to recieve all of the criteria
#Function to retry? Recieve feedback sends message on rabbitmq channel
#Returns a class of names, ids and urls
#Will be sending back at least 4 items at a time which is going to be an issue
#Make a function to add together all of the criteria scores together to see the best fit

@recomRouter.get("/{cloth}/get")
async def get_all(cloth: str):
    try:
        data = list(db[cloth].find())
        return all_items(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching {cloth}: {e}")

@recomRouter.get("/{c1}/{c2}/{c3}/{c4}/getrecom")
async def get_recom(c1: str,c2: str,c3: str,c4: str):
    try:
        recom = recom_return(retrieveBestItem(c1,c2,c3,c4,"jacket"),retrieveBestItem(c1,c2,c3,c4,"shirts"),retrieveBestItem(c1,c2,c3,c4,"trousers"),retrieveBestItem(c1,c2,c3,c4,"shoes"))
        return recom
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recommendation: {e}")


def retrieveBestItem(c1: str, c2: str, c3: str, c4: str, cloth: str):
    data = list(db[cloth].find())
    greatestValue = 0
    for item in data:
        if((item.get(c1)+item.get(c2)+item.get(c3)+item.get(c4))>greatestValue):
            greatestValue = (item.get(c1)+item.get(c2)+item.get(c3)+item.get(c4))
            bestItem = item_return(item)
    return bestItem



    