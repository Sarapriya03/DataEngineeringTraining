import fastapi

app = fastapi.FastAPI()

@app.get("/")
def home():
    return {"Message": "Hello from FastAPI"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"Message": f"Hello {name}!"}
