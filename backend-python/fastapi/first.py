from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":"blog list"}


@app.get("/blog")
def show(limit = 10,published : bool = True, sort : Optional[str] = None):
    if published:
        return {"data":f"blog list of {limit} published blogs"}
    else:
        return {"data":f"blog list of {limit} blogs"}


@app.get("/about")
def about():
    return{"data":{"quote":"Hello World"}}


@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished blogs"}


@app.get("/blog/{id}")
def show(id:int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def comments(id):
    return {"data":{'1','2'}}