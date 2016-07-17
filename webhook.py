from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class TwilioWebhook(BaseHTTPRequestHandler):
    def do_POST(self):
        # http://stackoverflow.com/a/2124520
        length = int(self.headers['Content-Length'])
        post_data = parse_qs(self.rfile.read(length).decode('utf-8'))

def setup_server():
    server_addr = ('', 80)
    httpd = HTTPServer(server_addr, TwilioWebhook)
    httpd.serve_forever()
