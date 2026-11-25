def clean_rooms(location, rooms):
    print(f"Initial location: {location}")
    print(f"Initial state: A={rooms['A']}, B={rooms['B']}")
    actions = 0

    while "dirty" in rooms.values():
        if rooms[location] == "dirty":
            print(f"Clean room {location}.")
            rooms[location] = "clean"
        else:
            next_room = "B" if location == "A" else "A"
            print(f"Move from {location} to {next_room}.")
            location = next_room
        actions += 1

    print(f"Final state: A={rooms['A']}, B={rooms['B']}")
    if location != "A":
        print(f"Move from {location} to A to recharge.")
        actions += 1
    print("Rest at the charging station in room A.")
    print(f"Cleaning and movement actions: {actions}")


location = input("Starting room (A/B): ").strip().upper()
state_a = input("Room A (clean/dirty): ").strip().lower()
state_b = input("Room B (clean/dirty): ").strip().lower()

if location not in {"A", "B"} or {state_a, state_b} - {"clean", "dirty"}:
    print("Invalid room or state.")
    raise SystemExit

clean_rooms(location, {"A": state_a, "B": state_b})
