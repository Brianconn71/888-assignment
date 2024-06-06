from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from sports import Sport, open_sports_json

# define a new app
app = FastAPI()

def get_sports_from_json():
    sports = open_sports_json()
    return sports

@app.get('/sports/')
def get_sports():
    return get_sports_from_json()


@app.get('/sports/{sport_id}', status_code=200)
def get_sports_by_id(sport_id: int):
    sport = get_sports_from_json()
    sports = [s for s in sport if s['id'] == sport_id]
    return sports[0] if len(sport) > 0 else {}


@app.get("/search", status_code=200)
def search_sport_by_name(name: Optional[str] = Query(None, title="Name", description="The name to filter results")):
    sports = get_sports_from_json()
    if name:
        return [s for s in sports if name.lower() in s['name'].lower()]
    return sports

@app.post('/sports/')
def get_sports():
    return {"sports": "Tennis"}

@app.get('/events/')
def get_events():
    return {"events": ["soccer", "basketball", "baseball", "hockey"]}

@app.get('/selections/')
def get_selections():
    return {"selections": ["soccer", "basketball", "baseball", "hockey"]}