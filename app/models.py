# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint
from typing import Optional

#----------------------------------Shirts Models------------------------------------------------

class recomClass(BaseModel):
    rec1_name:str
    rec2_name:str
    rec3_name:str
    rec4_name:str
    rec1_id:str
    rec2_id:str
    rec3_id:str
    rec4_id:str
    rec1_img_url:str
    rec2_img_url:str
    rec3_img_url:str
    rec4_img_url:str


def recom_return(rec1,rec2,rec3,rec4):
    return{
        "id1": str(rec1["id"]),
        "name1": rec1["name"],
        "img_url1": rec1["img_url"],
        "id2": str(rec2["id"]),
        "name2": rec2["name"],
        "img_url2": rec2["img_url"],
        "id3": str(rec3["id"]),
        "name3": rec3["name"],
        "img_url3": rec3["img_url"],
        "id4": str(rec4["id"]),
        "name4": rec4["name"],
        "img_url4": rec4["img_url"],
    }



#----------------------------------------------------------------- Clothes Read -------------------------------------------------------------------

class ItemClass(BaseModel):
    name:str
    brand:str
    light:      Optional[int] = None
    dark:       Optional[int] = None
    bright:     Optional[int] = None
    warm:       Optional[int] = None
    cool:       Optional[int] = None
    breathable: Optional[int] = None
    cozy:       Optional[int] = None
    lightweight:Optional[int] = None
    fancy:      Optional[int] = None
    casual:     Optional[int] = None
    business:   Optional[int] = None
    lounge:     Optional[int] = None
    evening:    Optional[int] = None
    minimalist: Optional[int] = None
    vintage:    Optional[int] = None
    modern:     Optional[int] = None
    soft:       Optional[int] = None
    comfortable:Optional[int] = None
    layerable:  Optional[int] = None
    img_url:str

def item_return(item):
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "brand": item["brand"],
        "light": item["light"],
        "dark": item["dark"],
        "bright": item["bright"],
        "warm": item["warm"],
        "cool": item["cool"],
        "lightweight": item["lightweight"],
        "fancy": item["fancy"],
        "casual": item["casual"],
        "business": item["business"],
        "lounge": item["lounge"],
        "evening": item["evening"],
        "minimalist": item["minimalist"],
        "vintage": item["vintage"],
        "modern": item["modern"],
        "soft": item["soft"],
        "comfortable": item["comfortable"],
        "layerable": item["layerable"],
        "img_url": item["img_url"]
    }

def all_items(all_items):
    return [item_return(item) for item in all_items]