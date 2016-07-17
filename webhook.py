from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn # can use ForkingMixIn instead to make a multi process system
from urllib.parse import parse_qs

# via https://github.com/Nakiami/MultithreadedSimpleHTTPServer
class WebhookServer(ThreadingMixIn, HTTPServer):
    pass

class Webhook(BaseHTTPRequestHandler):
    def do_POST(self):
        # it's in application/x-www-form-urlencoded format: via http://stackoverflow.com/a/2124520
        length = int(self.headers['Content-Length'])
        post_data = parse_qs(self.rfile.read(length).decode('utf-8'))

def setup_server():
    server_addr = ('', 80)
    httpd = WebhookServer(server_addr, Webhook)
    httpd.serve_forever()
