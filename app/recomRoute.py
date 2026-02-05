from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
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
async def get_recom(c1: str,c2: str,c3: str,c4: str,cloth: str):
    try:
        recom = recom_return(retrieveBestShirt(c1,c2,c3,c4),retrieveBestJacket(c1,c2,c3,c4),retrieveBestTrouser(c1,c2,c3,c4),retrieveBestShoes(c1,c2,c3,c4))
        return recom
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recommendation: {e}")


def retrieveBestShirt(c1: str, c2: str, c3: str, c4: str):
    data = list(db["shirts"].find())
    greatestValue = 0
    for item in data:
        if ((item.light + item.c2 + item.c3 + item.c4) > greatestValue):
            bestShirt = item.id
    shirt = (db["shirts"].find_one({"_id": ObjectId(bestShirt)}))
    return shirt

def retrieveBestJacket(c1: str, c2: str, c3: str, c4: str):
    data = list(db["jacket"].find())
    greatestValue = 0
    for item in data:
        if (item.c1 + item.c2 + item.c3 + item.c4 > greatestValue):
            bestJacket = item.id
    item1 = (db["jacket"].find_one({"_id": bestJacket}))
    return data

def retrieveBestTrouser(c1: str, c2: str, c3: str, c4: str):
    data = list(db["trousers"].find())
    greatestValue = 0
    for item in data:
        if (item.c1 + item.c2 + item.c3 + item.c4 > greatestValue):
            bestTrouser = item.id
    trousers = (db["trousers"].find_one({"_id": ObjectId(bestShoes)}))
    return trousers

def retrieveBestShoes(c1: str, c2: str, c3: str, c4: str):
    data = list(db["shoes"].find())
    greatestValue = 0
    for item in data:
        if (item.c1 + item.c2 + item.c3 + item.c4 > greatestValue):
            bestShoes = item.id
    shoes = (db["shoes"].find_one({"_id": ObjectId(bestShoes)}))
    return shoes
    