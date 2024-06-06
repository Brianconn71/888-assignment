from pydantic import BaseModel
from typing import Optional
import json


class Sport(BaseModel):
    Id: Optional[int]
    name: str
    slug: str
    active: bool


def open_sports_json():
    with open('../data/sports.json') as f:
        sport = json.load(f)['sports']
    return sport