from http.server import HTTPServer
import sys
import api.index as app  # import your Vercel handler

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    server = HTTPServer(("127.0.0.1", port), app.handler)
    print(f"Serving on http://127.0.0.1:{port}")
    server.serve_forever()
