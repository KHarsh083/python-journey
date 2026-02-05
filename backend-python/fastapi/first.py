from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":"blog list"}
@app.get("/about")
def about():
    return{"data":{"quote":"Hello World"}}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished blogs"}

@app.get("/blog/{id}")
def show(id:int):
    return {"data":id}