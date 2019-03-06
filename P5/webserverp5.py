import http.server
import socketserver

# Define the Server's port
PORT = 8001

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print('Request line:' + self.requestline)
        print('Command: ' + self.command)
        print('Path: ' + self.path)

        #handling possible requests
        req= self.path

        if req == '/':
            file = 'index.html'
        elif req == '/blue':
            file = 'blue.html'
        elif req == '/pink':
            file = 'pink.html'
        else:
            file = 'error.html'

        with open(file, 'r') as f:
            content=f.read()


        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Length-Type', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))


        return


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    #main program

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")