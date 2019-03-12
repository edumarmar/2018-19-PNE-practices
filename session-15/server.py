import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8002


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # printing the request line
        termcolor.cprint(self.requestline, 'green')

        # opening and reading the form1.html file
        f = open("form2.html", 'r')
        contents = f.read()

        # generating the response message
        self.send_response(200)

        # defining the header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return



# - Server MAIN program

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")