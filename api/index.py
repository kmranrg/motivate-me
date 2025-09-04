# /api/index.py
from http.server import BaseHTTPRequestHandler
import sqlite3, os, random, html

OWNER_NAME = "Kumar Anurag"
OWNER_LINK = "https://kmranrg.com"

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "quotes.db")
DB_URI = f"file:{DB_PATH}?mode=ro"

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
        bg = gradient_css()
        body = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Motivate Me</title>
<style>
  html,body{{height:100%;margin:0}}
  body{{display:flex;align-items:center;justify-content:center;background:{bg};
       font-family:system-ui,-apple-system,Segoe UI,Roboto,Inter,Arial,sans-serif;
       color:#fff;text-align:center}}
  .card{{max-width:820px;padding:40px 32px;background:rgba(0,0,0,.25);
        backdrop-filter:blur(6px);border-radius:24px;box-shadow:0 10px 40px rgba(0,0,0,.25)}}
  .quote{{font-size:2rem;line-height:1.3;margin:0 0 14px}}
  .author{{font-size:1.1rem;opacity:.9}}
  .footer{{position:fixed;left:0;right:0;bottom:0;padding:10px 14px;
           background:rgba(0,0,0,.35);backdrop-filter:blur(4px);
           font-size:.85rem;letter-spacing:.2px}}
  a{{color:#fff;text-underline-offset:2px}}
  button.refresh{{margin-top:22px;padding:10px 16px;border:0;border-radius:999px;
                 background:rgba(255,255,255,.22);color:#fff;font-weight:600;cursor:pointer}}
  button.refresh:hover{{background:rgba(255,255,255,.3)}}
</style>
</head>
<body>
  <div class="card">
    <p class="quote">&ldquo;{html.escape(text)}&rdquo;</p>
    <p class="author">&mdash; {html.escape(author)}</p>
    <form><button class="refresh" type="submit">New Quote ↻</button></form>
  </div>
  <div class="footer">
    Motivate Me • Built by
    <a href="{html.escape(OWNER_LINK)}" target="_blank" rel="noopener">{html.escape(OWNER_NAME)}</a>
  </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))
