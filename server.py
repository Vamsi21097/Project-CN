#took reference from https://www.afternerd.com/blog/python-http-server/
import http.server
import socketserver

# PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

# import SimpleHTTPServer
# import SocketServer

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print ("serving at port", PORT)
httpd.serve_forever()