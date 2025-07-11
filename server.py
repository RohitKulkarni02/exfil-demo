from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class ExfilServer(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode()
        print(f"[✅ EXFILTRATED]: {body}")
        self.send_response(200)
        self.end_headers()

print("🚨 Server on port 8080")
HTTPServer(("", 8080), ExfilServer).serve_forever()

