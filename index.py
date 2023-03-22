from fastapi import FastAPI
from routes.item import item

tags_metadata = [
        {
        "name": "Items", 
        "description": "Manage items.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(item)