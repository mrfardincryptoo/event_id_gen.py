import uuid

def generate_event_id():
    # Generates a unique UUID for event logging
    return str(uuid.uuid4())

print(f"New Event ID: {generate_event_id()}")
