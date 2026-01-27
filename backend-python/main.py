from fastapi import FastAPI

# create FastAPI app instance
app = FastAPI(
    title="Backend Python API",
    description="My first FastAPI backend",
    version="1.0.0"
)

# root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI is running 🚀"}

# simple health check
@app.get("/health")
def health():
    return {"status": "ok"}

# path parameter example
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"greeting": f"Hello, {name}!"}

# query parameter example
@app.get("/add")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b
    }
