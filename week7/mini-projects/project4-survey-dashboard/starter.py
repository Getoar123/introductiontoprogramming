import csv
import sqlite3

# -----------------------------
# 1. CREATE DATABASE
# -----------------------------
conn = sqlite3.connect("survey.db")
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS responses
""")

cur.execute("""
CREATE TABLE responses (
    student_id TEXT,
    faculty TEXT,
    year INTEGER,
    satisfaction INTEGER,
    favourite_tool TEXT,
    comments TEXT
)
""")

# -----------------------------
# 2. LOAD CSV FILES
# -----------------------------
files = [
    "faculty_science.csv",
    "faculty_arts.csv",
    "faculty_business.csv"
]

for filename in files:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute("""
                INSERT INTO responses 
                (student_id, faculty, year, satisfaction, favourite_tool, comments)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row["student_id"],
                row["faculty"],
                int(row["year"]),
                int(row["satisfaction"]),
                row["favourite_tool"],
                row["comments"]
            ))

conn.commit()

# -----------------------------
# 3. DASHBOARD QUERIES
# -----------------------------

print("\n==============================")
print("  UNIVERSITY SURVEY DASHBOARD")
print("==============================\n")

# 1. Responses by faculty
print("1. Total Responses by Faculty")
rows = cur.execute("""
    SELECT faculty, COUNT(*) 
    FROM responses
    GROUP BY faculty
""").fetchall()

total = 0
for row in rows:
    print(f"   {row[0]:8}: {row[1]}")
    total += row[1]
print(f"   TOTAL   : {total}\n")

# 2. Avg satisfaction by year
print("2. Average Satisfaction by Year of Study")
rows = cur.execute("""
    SELECT year, AVG(satisfaction)
    FROM responses
    GROUP BY year
    ORDER BY year
""").fetchall()

for row in rows:
    print(f"   Year {row[0]} : {row[1]:.1f} / 5")
print()

# 3. Favourite tool popularity
print("3. Favourite Tool Popularity")
rows = cur.execute("""
    SELECT favourite_tool, COUNT(*)
    FROM responses
    GROUP BY favourite_tool
    ORDER BY COUNT(*) DESC
""").fetchall()

for row in rows:
    print(f"   {row[0]:6}: {row[1]} students")
print()

# 4. Faculty comparison
print("4. Faculty Comparison")
rows = cur.execute("""
    SELECT faculty,
           AVG(satisfaction),
           favourite_tool,
           COUNT(favourite_tool) as tool_count
    FROM responses
    GROUP BY faculty
""").fetchall()

for row in rows:
    faculty = row[0]
    avg_sat = row[1]

    # most popular tool per faculty (simple version)
    tool = cur.execute("""
        SELECT favourite_tool
        FROM responses
        WHERE faculty = ?
        GROUP BY favourite_tool
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """, (faculty,)).fetchone()[0]

    print(f"   {faculty:<8} | {avg_sat:.1f}             | {tool}")
print()

# -----------------------------
# 5. INTERACTIVE QUERY
# -----------------------------

score = int(input("Enter minimum satisfaction score (1-5): "))

print("Students with satisfaction >= 5:")

rows = cur.execute("""
    SELECT student_id, faculty, year, favourite_tool
    FROM responses
    WHERE satisfaction >= ?
""", (score,)).fetchall()

for row in rows:
    print(f"   {row[0]} | {row[1]:8} | Year {row[2]} | {row[3]}")

conn.close()
