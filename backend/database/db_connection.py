import json
import os

FILE = "data/sessions.json"

def load_sessions():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_session(session):
    sessions = load_sessions()
    sessions.append(session)
    with open(FILE, "w") as f:
        json.dump(sessions, f, indent=2)
