import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

# Load the JSON data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(self.path.split('?')[-1])
        names = params.get("name", [])
        marks = [data.get(name, 0) for name in names]
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        response = { "marks": marks }
        self.wfile.write(json.dumps(response).encode())
