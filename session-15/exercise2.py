import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8001

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # printing the request line
        termcolor.cprint(self.requestline, 'green')
        print('Path: ' + self.path)

        path= self.path

        i=path.find('=')


        if self.path== '/' or self.path=='/echo':
            f = open("form_exercise2.html", 'r')
            content = f.read()

            print('Path: ' + self.path)

            path = self.path

            i = path.find('=')

        else:
            f = open("error.html", 'r')
            content = f.read()


        if i != -1:

            if path.find('&') != -1:
                i2 = path.find('&')
                msg = path[i + 1: i2]
                msg = msg.upper()
                msg = msg.replace('+', ' ')
            else:
                msg = path[i + 1:]

            f = open('echohtml.html', 'r')
            content = f.read()
            content = content.replace('msg', msg)

        # generating the response message
        self.send_response(200)

        # defining the header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(content))

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