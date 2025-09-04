# /api/index.py
from http.server import BaseHTTPRequestHandler
import sqlite3, os, random, html
from string import Template

OWNER_NAME = "Kumar Anurag"
OWNER_LINK = "https://kmranrg.com"

ROOT = os.path.join(os.path.dirname(__file__), "..")
DB_PATH = os.path.join(ROOT, "quotes.db")
DB_URI = f"file:{DB_PATH}?mode=ro"
TEMPLATE_PATH = os.path.join(ROOT, "templates", "index.html")

# Cache the compiled template at import time (fast + works on Vercel)
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    PAGE = Template(f.read())

def get_random_quote():
    with sqlite3.connect(DB_URI, uri=True, check_same_thread=False) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT text, author FROM quotes ORDER BY RANDOM() LIMIT 1"
        ).fetchone()
        if row:
            return row["text"], row["author"]
        return ("Stay positive, work hard, make it happen.", "Unknown")

def gradient_css():
    angle = random.randint(0, 360)
    def hsl():
        return f"hsl({random.randint(0,360)}, {random.randint(55,85)}%, {random.randint(35,60)}%)"
    return f"linear-gradient({angle}deg, {hsl()}, {hsl()})"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        text, author = get_random_quote()
        body = PAGE.substitute(
            bg=gradient_css(),
            quote=html.escape(text),
            author=html.escape(author),
            owner_link=html.escape(OWNER_LINK),
            owner_name=html.escape(OWNER_NAME),
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))
