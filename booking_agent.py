def book_appointment(provider):
    print(f"Booking slot with {provider['name']}")
    return {"status": "booked", "slot": provider["slot"]}
