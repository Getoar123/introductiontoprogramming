import sqlite3

# Connect to database
conn = sqlite3.connect("favorites.db")
cursor = conn.cursor()

while True:
    print("\n--- SQL Explorer ---")
    print("1. Count all rows")
    print("2. Show language counts")
    print("3. Show most popular language")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        cursor.execute("SELECT COUNT(*) FROM favorites;")
        print("Total rows:", cursor.fetchone()[0])

    elif choice == "2":
        cursor.execute("""
            SELECT language, COUNT(*) 
            FROM favorites 
            GROUP BY language;
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}")

    elif choice == "3":
        cursor.execute("""
            SELECT language, COUNT(*) AS n
            FROM favorites
            GROUP BY language
            ORDER BY n DESC
            LIMIT 1;
        """)
        row = cursor.fetchone()
        print(f"Most popular: {row[0]} ({row[1]})")

    elif choice == "4":
        break

    else:
        print("Invalid choice")

conn.close()
