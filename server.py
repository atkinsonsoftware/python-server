from http.server import SimpleHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
port = 8080

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "test.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("POST, Path: %s, Headers: %s,\nBody:%s",
            str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, port), MyServer)
    print("Server started http://%s:%s" % (hostName, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
