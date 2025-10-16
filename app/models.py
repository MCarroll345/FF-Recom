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

def return_value2(shirts,value):
    return [shirt_return(shirt) for shirt in shirts if (shirt.get("test_value2") == value)]


def all_shirts(shirts):
    return [shirt_return(shirt) for shirt in shirts]