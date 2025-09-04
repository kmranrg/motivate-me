# /scripts/seed_db.py
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "quotes.db")

QUOTES = [
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("It always seems impossible until it’s done.", "Nelson Mandela"),
    ("Whether you think you can or you think you can’t, you’re right.", "Henry Ford"),
    ("Do something today that your future self will thank you for.", "Sean Patrick Flanery"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier"),
    ("Hard choices, easy life. Easy choices, hard life.", "Jerzy Gregorek"),
    ("The best way out is always through.", "Robert Frost"),
    ("What you do every day matters more than what you do once in a while.", "Gretchen Rubin"),
    ("We are what we repeatedly do. Excellence, then, is not an act but a habit.", "Will Durant"),
    ("You miss 100% of the shots you don’t take.", "Wayne Gretzky"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("If you’re going through hell, keep going.", "Winston Churchill"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("If not now, when?", "Hillel the Elder"),
    ("Everything you’ve ever wanted is on the other side of fear.", "George Addair"),
    ("Opportunity is missed by most people because it is dressed in overalls and looks like work.", "Thomas Edison"),
    ("Start where you are. Use what you have. Do what you can.", "Arthur Ashe"),
    ("Don’t wish it were easier; wish you were better.", "Jim Rohn"),
    ("If you want to lift yourself up, lift up someone else.", "Booker T. Washington"),
    ("Action is the foundational key to all success.", "Pablo Picasso"),
    ("What we fear doing most is usually what we most need to do.", "Tim Ferriss"),
    ("A year from now you may wish you had started today.", "Karen Lamb"),
    ("Make each day your masterpiece.", "John Wooden"),
    ("Well done is better than well said.", "Benjamin Franklin"),
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("Energy and persistence conquer all things.", "Benjamin Franklin"),
    ("If opportunity doesn’t knock, build a door.", "Milton Berle"),
    ("I am not a product of my circumstances. I am a product of my decisions.", "Stephen R. Covey"),
    ("Motivation is what gets you started. Habit is what keeps you going.", "Jim Ryun"),
    ("If you can’t yet do great things, do small things in a great way.", "Napoleon Hill"),
    ("What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Ralph Waldo Emerson"),
    ("Discipline equals freedom.", "Jocko Willink"),
    ("Little by little, a little becomes a lot.", "Tanzanian Proverb"),
    ("He who has a why to live can bear almost any how.", "Friedrich Nietzsche"),
    ("Courage is not the absence of fear, but the triumph over it.", "Nelson Mandela"),
    ("Simplicity is the ultimate sophistication.", "Leonardo da Vinci"),
    ("Doubt kills more dreams than failure ever will.", "Suzy Kassem"),
    ("The man who moves a mountain begins by carrying away small stones.", "Confucius"),
    ("If you get tired, learn to rest, not to quit.", "Banksy"),
    ("Fall seven times, stand up eight.", "Japanese Proverb"),
]

def main():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS quotes")
    c.execute("""CREATE TABLE quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text   TEXT NOT NULL,
        author TEXT NOT NULL
    )""")
    c.executemany("INSERT INTO quotes (text, author) VALUES (?, ?)", QUOTES)
    conn.commit()
    conn.close()
    print(f"Created {DB_PATH} with {len(QUOTES)} quotes.")

if __name__ == "__main__":
    main()
