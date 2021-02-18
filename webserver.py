# reference : https://www.youtube.com/watch?v=kogOfxg1c_g&ab_channel=ConorBailey

from http.server import HTTPServer, BaseHTTPRequestHandler

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        # self.wfile.write(self.path[1:].encode())
        f = open('index.html','rb')
        print(self.path)
        if('.html' not in self.path[1:]):
            self.send_response(400)
            o=''
            o+='<html><body>'
            o+='<h1>400 Bad Request</h1>'
            o+='</body></html>'
            self.wfile.write(o.encode())
        elif(self.path[1:]!='index.html'):            
            self.send_response(403)
            o=''
            o+='<html><body>'
            o+='<h1>403 Forbidden Page</h1>'
            o+='</body></html>'
            self.wfile.write(o.encode())
        elif(self.path[1:]=='index.html'):
            self.wfile.write(f.read())
        

def main():
    PORT=8000
    server=HTTPServer(('',PORT),helloHandler)
    print("Server running on port %s" %PORT)
    server.serve_forever()

if __name__=='__main__':
    main()
