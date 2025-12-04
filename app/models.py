# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint

#----------------------------------Shirts Models------------------------------------------------

class ShirtClass(BaseModel):
    name:str
    brand:str
    image_url:str
    test_value1:int
    test_value2:int
    test_value3:int


def shirt_return(shirt):
    return{
        "id": str(shirt["_id"]),
        "name": shirt["name"],
        "brand": shirt["brand"],
        "img_url": shirt["img_url"],
        "test_value1": shirt["test_value1"],
        "test_value2": shirt["test_value2"],
        "test_value3": shirt["test_value3"]
    }

def return_value2(all_shirts,value):
    return [shirt_return(shirt) for shirt in all_shirts if (shirt.get("test_value2") == value)]


def all_shirts(all_shirts):
    return [shirt_return(shirt) for shirt in all_shirts]

#----------------------------------Trousers Models------------------------------------------------

class TrouserClass(BaseModel):
    name:str
    brand:str
    image_url:str
    test_value1:int
    test_value2:int
    test_value3:int


def trouser_return(trouser):
    return{
        "id": str(trouser["_id"]),
        "name": trouser["name"],
        "brand": trouser["brand"],
        "img_url": trouser["img_url"],
        "test_value1": trouser["test_value1"],
        "test_value2": trouser["test_value2"],
        "test_value3": trouser["test_value3"]
    }

def return_value2(all_trousers,value):
    return [trouser_return(trouser) for trouser in all_trousers if (trouser.get("test_value2") == value)]


def all_trousers(all_trousers):
    return [trouser_return(trouser) for trouser in all_trousers]

#----------------------------------Dress Models------------------------------------------------

class DressClass(BaseModel):
    name:str
    brand:str
    image_url:str
    test_value1:int
    test_value2:int
    test_value3:int


def dress_return(dress):
    return{
        "id": str(dress["_id"]),
        "name": dress["name"],
        "brand": dress["brand"],
        "img_url": dress["img_url"],
        "test_value1": dress["test_value1"],
        "test_value2": dress["test_value2"],
        "test_value3": dress["test_value3"]
    }

def return_value2(all_dresses,value):
    return [dress_return(dress) for dress in all_dresses if (dress.get("test_value2") == value)]


def all_dresses(all_dresses):
    return [dress_return(dress) for dress in all_dresses]

#----------------------------------Jackets Models------------------------------------------------

class JacketClass(BaseModel):
    name:str
    brand:str
    image_url:str
    test_value1:int
    test_value2:int
    test_value3:int


def jacket_return(jacket):
    return{
        "id": str(jacket["_id"]),
        "name": jacket["name"],
        "brand": jacket["brand"],
        "img_url": jacket["img_url"],
        "test_value1": jacket["test_value1"],
        "test_value2": jacket["test_value2"],
        "test_value3": jacket["test_value3"]
    }

def return_value2(all_jackets,value):
    return [jacket_return(jacket) for jacket in all_jackets if (jacket.get("test_value2") == value)]


def all_jackets(all_jackets):
    return [jacket_return(jacket) for jacket in all_jackets]

#----------------------------------Shoes Models------------------------------------------------

class ShoeClass(BaseModel):
    name:str
    brand:str
    image_url:str
    test_value1:int
    test_value2:int
    test_value3:int


def shoe_return(shoe):
    return{
        "id": str(shoe["_id"]),
        "name": shoe["name"],
        "brand": shoe["brand"],
        "img_url": shoe["img_url"],
        "test_value1": shoe["test_value1"],
        "test_value2": shoe["test_value2"],
        "test_value3": shoe["test_value3"]
    }

def return_value2(all_shoes,value):
    return [shoe_return(shoe) for shoe in all_shoes if (shoe.get("test_value2") == value)]


def all_shoes(all_shoes):
    return [shoe_return(shoe) for shoe in all_shoes]

#----------------------------------Skirts Models------------------------------------------------

class SkirtClass(BaseModel):
    name:str
    brand:str
    image_url:str
    test_value1:int
    test_value2:int
    test_value3:int


def skirt_return(skirt):
    return{
        "id": str(skirt["_id"]),
        "name": skirt["name"],
        "brand": skirt["brand"],
        "img_url": skirt["img_url"],
        "test_value1": skirt["test_value1"],
        "test_value2": skirt["test_value2"],
        "test_value3": skirt["test_value3"]
    }

def return_value2(all_skirts,value):
    return [skirt_return(skirt) for skirt in all_skirts if (skirt.get("test_value2") == value)]


def all_skirts(all_skirts):
    return [skirt_return(skirt) for skirt in all_skirts]