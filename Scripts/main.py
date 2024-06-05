from fastapi import FastAPI
from pydantic import BaseModel

# define a new app
app = FastAPI()

@app.get('/sports/')
def get_sports():
    return {"sports": ["soccer", "basketball", "baseball", "hockey"]}

@app.post('/sports/')
def get_sports():
    return {"sports": "Tennis"}

@app.get('/events/')
def get_events():
    return {"events": ["soccer", "basketball", "baseball", "hockey"]}

@app.get('/selections/')
def get_selections():
    return {"selections": ["soccer", "basketball", "baseball", "hockey"]}