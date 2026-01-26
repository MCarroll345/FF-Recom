# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint

#----------------------------------Shirts Models------------------------------------------------

class ShirtClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int
    img_url:str


def item_return(item):
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "brand": item["brand"],
        "test_value1": item["test_value1"],
        "test_value2": item["test_value2"],
        "test_value3": item["test_value3"],
        "img_url": item["img_url"]
    }

def return_value2(all_shirts,value):
    return [shirt_return(shirt) for shirt in all_shirts if (shirt.get("test_value2") == value)]


def all_items(all_items):
    return [item_return(item) for item in all_items]

#----------------------------------Trousers Models------------------------------------------------

class TrouserClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int
    img_url:str


def trouser_return(trouser):
    return{
        "id": str(trouser["_id"]),
        "name": trouser["name"],
        "brand": trouser["brand"],
        "test_value1": trouser["test_value1"],
        "test_value2": trouser["test_value2"],
        "test_value3": trouser["test_value3"],
        "img_url": trouser["img_url"]
    }

def return_value2(all_trousers,value):
    return [trouser_return(trouser) for trouser in all_trousers if (trouser.get("test_value2") == value)]


def all_trousers(all_trousers):
    return [trouser_return(trouser) for trouser in all_trousers]

#----------------------------------Dress Models------------------------------------------------

class DressClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int
    img_url:str


def dress_return(dress):
    return{
        "id": str(dress["_id"]),
        "name": dress["name"],
        "brand": dress["brand"],
        "test_value1": dress["test_value1"],
        "test_value2": dress["test_value2"],
        "test_value3": dress["test_value3"],
        "img_url": dress["img_url"]
    }

def return_value2(all_dresses,value):
    return [dress_return(dress) for dress in all_dresses if (dress.get("test_value2") == value)]


def all_dresses(all_dresses):
    return [dress_return(dress) for dress in all_dresses]

#----------------------------------Jackets Models------------------------------------------------

class JacketClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int
    img_url:str


def jacket_return(jacket):
    return{
        "id": str(jacket["_id"]),
        "name": jacket["name"],
        "brand": jacket["brand"],
        "test_value1": jacket["test_value1"],
        "test_value2": jacket["test_value2"],
        "test_value3": jacket["test_value3"],
        "img_url": jacket["img_url"]
    }

def return_value2(all_jackets,value):
    return [jacket_return(jacket) for jacket in all_jackets if (jacket.get("test_value2") == value)]


def all_jackets(all_jackets):
    return [jacket_return(jacket) for jacket in all_jackets]

#----------------------------------Shoes Models------------------------------------------------

class ShoeClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int
    img_url:str


def shoe_return(shoe):
    return{
        "id": str(shoe["_id"]),
        "name": shoe["name"],
        "brand": shoe["brand"],
        "test_value1": shoe["test_value1"],
        "test_value2": shoe["test_value2"],
        "test_value3": shoe["test_value3"],
        "img_url": shoe["img_url"]
    }

def return_value2(all_shoes,value):
    return [shoe_return(shoe) for shoe in all_shoes if (shoe.get("test_value2") == value)]


def all_shoes(all_shoes):
    return [shoe_return(shoe) for shoe in all_shoes]

#----------------------------------Skirts Models------------------------------------------------

class SkirtClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int
    img_url:str


def skirt_return(skirt):
    return{
        "id": str(skirt["_id"]),
        "name": skirt["name"],
        "brand": skirt["brand"],
        "test_value1": skirt["test_value1"],
        "test_value2": skirt["test_value2"],
        "test_value3": skirt["test_value3"],
        "img_url": skirt["img_url"]
    }

def return_value2(all_skirts,value):
    return [skirt_return(skirt) for skirt in all_skirts if (skirt.get("test_value2") == value)]


def all_skirts(all_skirts):
    return [skirt_return(skirt) for skirt in all_skirts]