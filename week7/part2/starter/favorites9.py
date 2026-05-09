from cs50 import SQL

# Open the database
db = SQL("sqlite:///favorites.db")

# Run SQL query
rows = db.execute("""
    SELECT language, COUNT(*) AS n
    FROM favorites
    GROUP BY language
    ORDER BY n DESC;
""")

# Print results
for row in rows:
    print(f"{row['language']} {row['n']}")
