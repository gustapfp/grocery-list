from fastapi import FastAPI
from routes import item, user
# from routes.user import user

tags_metadata = [
        {
        "name": "Items", 
        "description": "Manage items.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(item.item)
app.include_router(user.user)