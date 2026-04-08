from pydantic import BaseModel
from typing import List

class Email(BaseModel):
    id: int
    content: str
    status: str
    priority: int

class Observation(BaseModel):
    inbox: List[Email]
    satisfaction: float
    step_count: int

class Action(BaseModel):
    type: str
    email_id: int
    content: str = ""