def parse_task(task: str) -> dict:
    # Dummy parser for demo
    if "dermatologist" in task:
        return {
            "specialty": "dermatologist",
            "location": "nearby",
            "action": "book_appointment"
        }
    return {"error": "Unrecognized task"}
