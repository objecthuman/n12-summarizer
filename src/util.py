import json
import os

# Message store path
os.makedirs("data", exist_ok=True)
MESSAGE_STORE = "data/messages.json"

def load_messages():
    if not os.path.exists(MESSAGE_STORE):
        return []
    with open(MESSAGE_STORE, "r") as f:
        return json.load(f) #reads messages.json and returns a python list,gets previously saved message


def save_message(entry: str):
    messages = load_messages()
    messages.append(entry) #updates with any new entry 

    with open(MESSAGE_STORE, "w") as f:
        json.dump(messages[-100:], f, indent=2)  # Keep last 100 messages
    


