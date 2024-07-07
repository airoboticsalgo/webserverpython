from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import  json
import urllib.parse
import logging
hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # print(self.parse_request.)
        # self.send_response(200)
        # self.send_header("Content-type", "text/html")
        # self.end_headers()
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))
        # def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')
    def do_POST(self):
        print("path=",self.path.startswith('/time'))
        if self.path.startswith('/time'):
        
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            print("body",body)
            print("urlparse=",urllib.parse.parse_qs(urllib.parse.urlparse(str(self.path)).query))
            ss=urllib.parse.parse_qs(urllib.parse.urlparse(str(self.path)).query)['test'][0]


            s=f"KEY={ss}"

            logging.info(s)
            # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(body)

if __name__ == "__main__":        
    logging.basicConfig(level=logging.INFO)
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")