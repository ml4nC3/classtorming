import logging
from random import randint
from models import attendee


class Session:
    """Session class handles the ability to interact with storming sessions, activities, attendees..."""
    def __init__(self):
        self.session_id = str()
        self.attendees = list()
        for num in range(6):
            self.session_id += str(randint(0, 9))
        # TODO: Ouvrir une socket

    def add_activity(self, activity_type):
        logging.info(f"Creating new activity {activity_type} in session_id={self.session_id}")
        return True

    def add_attendee(self, attendee: attendee.Attendee):
        self.attendees.append(attendee)
        # TODO: Envoyer le nouvel arrivant sur la socket prof
        # TODO: Ouvrir une socket avec le participant



