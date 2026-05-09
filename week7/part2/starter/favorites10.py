from cs50 import SQL

db = SQL("sqlite:///favorites.db")

# Ask user for input
favorite = input("Favorite: ")

# Parameterised query (safe from SQL injection)
rows = db.execute(
    "SELECT COUNT(*) AS n FROM favorites WHERE problem = ?",
    favorite
)

# Get result (only one row)
row = rows[0]

# Print count
print(row["n"])
