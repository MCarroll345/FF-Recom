# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint

class ShirtClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int


def shirt_return(shirt):
    return{
        "id": str(shirt["_id"]),
        "name": shirt["name"],
        "brand": shirt["brand"],
        "test_value1": shirt["test_value1"],
        "test_value2": shirt["test_value2"],
        "test_value3": shirt["test_value3"]
    }

def return_value2(all_shirts,value):
    return [shirt_return(shirt) for shirt in all_shirts if (shirt.get("test_value2") == value)]


def all_shirts(all_shirts):
    return [shirt_return(shirt) for shirt in all_shirts]

class TrouserClass(BaseModel):
    name:str
    brand:str
    test_value1:int
    test_value2:int
    test_value3:int


def trouser_return(trouser):
    return{
        "id": str(trouser["_id"]),
        "name": trouser["name"],
        "brand": trouser["brand"],
        "test_value1": trouser["test_value1"],
        "test_value2": trouser["test_value2"],
        "test_value3": trouser["test_value3"]
    }

def return_value2(all_trousers,value):
    return [trouser_return(trouser) for trouser in all_trousers if (trouser.get("test_value2") == value)]


def all_trousers(all_trousers):
    return [trouser_return(trouser) for trouser in all_trousers]