
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        body = b"Hello from Docker! This is Linux lab2.\n"

        self.send_response(200)

        self.send_header("Content-Type", "text/plain; charset=utf-8")

        self.send_header("Content-Length", str(len(body)))

        self.end_headers()

        self.wfile.write(body)

    def log_message(self, fmt, *args):

        print("request:", self.path)

if __name__ == "__main__":

    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()

