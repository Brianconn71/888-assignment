from pydantic import BaseModel
from typing import Optional, List
from events import Event
import json


class Selection(BaseModel):
    id: Optional[int]
    name: str
    active: bool
    event: Optional[List[Event]]
    price: float
    outcome: str


with open('../data/selections.json') as f:
    selection = json.load(f)['selections']

print(selection)