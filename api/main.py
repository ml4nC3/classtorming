from typing import Optional
from fastapi import FastAPI
from random import randint
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
    logging.info(f"Creating new session with session_id={self.session_id}")
    return new_session.session_id

# Connect to session from attendee app
@app.get("/connect/session")
def connect_session():


@app.get("/{session_id}/startactivity/{activity_type}")
def create_activity(session_id: str, activity_type: str):
    current_session = sessions[session_id]
    current_session.add_activity(activity_type)
    return True


class Session:
    """Session class handles the ability to interact with storming sessions, activities, attendees..."""
    def __init__(self):
        self.session_id = str()
        for num in range(6):
            self.session_id += str(randint(0, 9))

    def add_activity(self, activity_type):
        logging.info(f"Creating new activity {activity_type} in session_id={self.session_id}")
        return True

