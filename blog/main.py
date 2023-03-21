from fastapi import FastAPI
from schemas import Blog


app = FastAPI()



@app.post("/")
async def create_blog(blog: Blog):
    return blog