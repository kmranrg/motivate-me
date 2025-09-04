# /scripts/seed_db.py
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "quotes.db")

quotes = [
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("It always seems impossible until it’s done.", "Nelson Mandela"),
    ("Whether you think you can or you think you can’t, you’re right.", "Henry Ford"),
    ("Do something today that your future self will thank you for.", "Sean Patrick Flanery"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier"),
    ("Hard choices, easy life. Easy choices, hard life.", "Jerzy Gregorek"),
    ("The best way out is always through.", "Robert Frost"),
]

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS quotes")
c.execute("""CREATE TABLE quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text   TEXT NOT NULL,
    author TEXT NOT NULL
)""")
c.executemany("INSERT INTO quotes (text, author) VALUES (?, ?)", quotes)
conn.commit()
conn.close()
print(f"Created {DB_PATH} with {len(quotes)} quotes.")
