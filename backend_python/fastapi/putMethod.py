from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel

app =FastAPI()
@app.get("/")
def index():
    return {"data":"blog list"}

class Blog(BaseModel):
    title : str
    body: str
    publishedAt : Optional[bool]


@app.post('/blog')
def create_blog(request : Blog):
    return {'data':f'blog is created with title {request.title}'}

