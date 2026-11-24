from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class InventoryHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/items":
            items = [
                {
                    "name": "Network Cable",
                    "department": "Administration",
                    "quantity": 500
                },
                {
                    "name": "Steel Sheet",
                    "department": "Production",
                    "quantity": 75
                }
            ]

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(items).encode())

        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 8000), InventoryHandler)

print("Inventory API running on port 8000")

server.serve_forever()
