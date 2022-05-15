from fastapi import FastAPI

app = FastAPI()

@app.get('/index')
def index():
    return {"Hello": "World"}

@app.get('/')
def index():
    return {"Good": "Morning"}