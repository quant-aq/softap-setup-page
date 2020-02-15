import http.server
import socketserver
import os

PORT = 8000
STATIC_DIR = "src"

os.chdir(STATIC_DIR)
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print ("Serving at http://localhost:" + str(PORT))
httpd.serve_forever()