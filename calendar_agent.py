def add_to_calendar(appointment):
    print(f"Adding appointment to calendar on {appointment['slot']}")
    return {"calendar_event": "created", "slot": appointment["slot"]}
