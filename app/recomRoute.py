from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from bson import ObjectId
from .models import *
from .config import db
from .publish import get_rabbitmq_publisher

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
        recom = collect_items(c1,c2,c3,c4)
        return recom
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recommendation: {e}")

def collect_items(c1: str, c2: str, c3: str, c4: str):
    rec1 = retrieveBestItem(c1,c2,c3,c4,"shirts")
    rec2 = retrieveBestItem(c1,c2,c3,c4,"trousers")
    rec3 = retrieveBestItem(c1,c2,c3,c4,"shoes")
    rec4 = retrieveBestItem(c1,c2,c3,c4,"jacket")

    if not all([rec1, rec2, rec3, rec4]):
        return {"error": "No recommendation found"}

    publisher = get_rabbitmq_publisher()
    publisher.pubRecom(
        "recom_topic",
        "recom_queue",
        pub_recom_return(rec1,rec2,rec3,rec4,c1,c2,c3,c4,1)
    )

    return recom_return(rec1,rec2,rec3,rec4)


def retrieveBestItem(c1: str, c2: str, c3: str, c4: str, cloth: str):
    data = list(db[cloth].find())
    greatestValue = 0
    bestItem = None
    for item in data:
        score = (item.get(c1, 0) + item.get(c2, 0) + item.get(c3, 0) + item.get(c4, 0))
        if score > greatestValue:
            greatestValue = score
            bestItem = item_return(item)
    
    return bestItem



    