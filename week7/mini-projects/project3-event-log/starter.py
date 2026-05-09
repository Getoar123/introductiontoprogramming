import csv

# Data structures
room_counts = {}
type_counts = {}
day_attendees = {}
large_events = []

with open("bookings.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["date"]
        room = row["room"]
        event_type = row["event_type"]
        attendees = int(row["attendees"])

        # 1. Bookings by room
        room_counts[room] = room_counts.get(room, 0) + 1

        # 2. Bookings by event type
        type_counts[event_type] = type_counts.get(event_type, 0) + 1

        # 3. Busiest day (sum attendees per day)
        day_attendees[date] = day_attendees.get(date, 0) + attendees

        # 4. Large events (> 50 attendees)
        if attendees > 50:
            large_events.append({
                "date": date,
                "room": room,
                "event_type": event_type,
                "attendees": attendees
            })

# Find busiest day
busiest_day = max(day_attendees, key=day_attendees.get)

# Sort large events by attendees descending
large_events.sort(key=lambda x: x["attendees"], reverse=True)

# Output
print("=== Community Centre Booking Report ===\n")

print("Bookings by Room:")
for room in sorted(room_counts):
    print(f"  {room} : {room_counts[room]} events")

print("\nBookings by Event Type:")
for event_type in sorted(type_counts):
    print(f"  {event_type:<8}: {type_counts[event_type]} events")

print(f"\nBusiest Day: {busiest_day}  ({day_attendees[busiest_day]} total attendees)\n")

print("Large Events (> 50 attendees):")
for event in large_events:
    print(f"  {event['date']} | {event['room']:<6} | {event['event_type']:<8} | {event['attendees']:>3} attendees")
