from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from .clothesRoutes.shirtRoute import shirtRouter
from .clothesRoutes.trouserRoute import trouserRouter

app = FastAPI()

app.include_router(shirtRouter)
app.include_router(trouserRouter)