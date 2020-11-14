from pydantic import BaseModel


class Attendee(BaseModel):
    name: str


