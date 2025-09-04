# Motivate Me

<img src="https://github.com/kmranrg/motivate-me/blob/main/icon.png" width=100>

Minimal motivational quotes app — **pure Python stdlib + SQLite (read-only)** — deployed on **Vercel (Hobby)**.  
Every refresh → new quote + fresh gradient. Installable **PWA**.

**Live:** [https://motivate-me-three.vercel.app/](https://motivate-me-three.vercel.app/?)

---

## Features
- Server-rendered Python (random quote + gradient per request)
- SQLite bundled as **read-only** (`quotes.db`)
- PWA: `manifest.webmanifest` + `sw.js`
- No frameworks: Python + HTML/CSS/vanilla JS

---

## Project Structure
```
├─ api/index.py # serverless function (reads template, queries SQLite)
├─ templates/index.html # HTML template ($placeholders via string.Template)
├─ scripts/seed_db.py # create/regenerate quotes.db
├─ quotes.db # bundled read-only SQLite
├─ icon.png # favicon/app icon
├─ manifest.webmanifest # PWA manifest
├─ sw.js # service worker
├─ local_server.py # local dev (serves static + /)
└─ vercel.json # "/" → /api/index.py
```

---

## Quick Start (Local)
```bash
# 1) Build DB
python scripts/seed_db.py

# 2) Run locally (serves / and static files)
python local_server.py
# → http://127.0.0.1:8000
