from typing import Optional
from fastapi import FastAPI
from models import attendee
from session import Session
import logging


logging.basicConfig(filename='classtorming-api.log',
                    level=logging.DEBUG,
                    format='%(asctime)s|%(levelname)s|%(name)s|%(threadName)s|%(message)s')

app = FastAPI()

sessions = dict()

activities = {"sondage": 1234,
              "tableau": 74938}


@app.get("/")
def read_root():
    return list(activities.keys())


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    return {"item_id": activities[item_id], "q": q}

# Create activity


# Start session
@app.get("/create/session")
def create_session():
    new_session = Session()
    sessions[new_session.session_id] = new_session
    logging.info(f"Creating new session with session_id={new_session.session_id}")
    return new_session.session_id


# Connect to session from attend app
@app.post("/{session_id}/connect")
async def connect_session(session_id: str, newcomer: attendee.Attendee):
    sessions[session_id].add_attendee(newcomer)
    return newcomer.name


@app.get("/{session_id}/startactivity/{activity_type}")
def create_activity(session_id: str, activity_type: str):
    current_session = sessions[session_id]
    current_session.add_activity(activity_type)
    return True


@app.get("/{session_id}/attendees")
def get_attendee_list(session_id: str):
    return sessions[session_id]

