from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

dir = os.path.dirname(__file__)
app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'Hello World'}

@app.get("/{day}")
async def getdata(day):
    file = open('new.json')
    path = os.path.join(dir, 'data/{filename}.json'.format(filename = day))

    if os.path.exists(path):
        file = open(path)
        return JSONResponse(json.load(file)) 

    return JSONResponse({'Error':'FileNotFound'})

