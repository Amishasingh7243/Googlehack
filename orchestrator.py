from agents.call_agent import initiate_call
from agents.booking_agent import book_appointment
from agents.calendar_agent import add_to_calendar


def orchestrate_task(data):
    provider = initiate_call(data["specialty"])
    appointment = book_appointment(provider)
    confirmation = add_to_calendar(appointment)
    return confirmation
