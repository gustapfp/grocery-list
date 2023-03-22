from fastapi import FastAPI
from routes.item import item

app = FastAPI()

app.include_router(item)