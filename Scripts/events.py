from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime as DateTime
from sports import Sport
import json


class Event(BaseModel):
    Id: Optional[int]
    name: str
    slug: str
    active: bool
    type: str
    sport: Optional[List[Sport]]
    status: str
    scheduled_start: DateTime
    actual_start: DateTime


with open('../data/events.json') as f:
    event = json.load(f)['events']

print(event)