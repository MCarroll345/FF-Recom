from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from .clothesRoutes.shirtRoute import shirtRouter
from .clothesRoutes.trouserRoute import trouserRouter
from .clothesRoutes.dressRoute import dressRouter
from .clothesRoutes.jacketRoute import jacketRouter
from .clothesRoutes.shoeRoute import shoeRouter
from .clothesRoutes.skirtRoute import skirtRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(shirtRouter)
app.include_router(trouserRouter)
app.include_router(dressRouter)
app.include_router(jacketRouter)
app.include_router(shoeRouter)
app.include_router(skirtRouter)