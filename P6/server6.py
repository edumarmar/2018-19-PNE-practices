import http.server
import socketserver
import termcolor
from Seqp6 import Seq

# Define the Server's port
PORT = 8001

# Class with oreur Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # printing the request line
        termcolor.cprint(self.requestline, 'green')
        print('Path: ' + self.path)

        #checking that the url is right
        if self.path== '/':
            f = open("dnaform.html", 'r')
            content = f.read()

        else:
            f = open("error.html", 'r')
            content = f.read()

        path = self.path

        i = path.find('=')

        if i != -1:
            #processing the message from the client with urllib
            from urllib import parse
            url = path
            parse.urlsplit(url)
            parse.parse_qs(parse.urlsplit(url).query)
            variables=dict(parse.parse_qsl(parse.urlsplit(url).query))
            print(variables)


            # checking that the sequence is alright
            seq= variables['msg']
            seq=seq.lower()
            check='acgt'
            correct = True
            for i in seq:
                if not i in check:
                    correct = False

            #calculating the results
            if  correct == True:

                seq = Seq(variables['msg'])
                finalmsg = ''
                try:
                    if variables['chk']=='on':
                        finalmsg+= '\n>The length of the sequence is: ' + str(seq.len())
                except:
                    pass

                if variables['operation']== 'count':
                    finalmsg += '\n>The count of '+ variables['base'] + ' is: ' + str(seq.count(variables['base']))
                elif variables['operation']== 'perc':
                    finalmsg += '\n>The percentage of '+ variables['base'] + ' is: ' + str(seq.perc(variables['base']))

                f = open('responsehtml.html', 'r')
                content = f.read()
                content = content.replace('msg', finalmsg)
            elif correct==False:
                f = open('errorsequence.html', 'r')
                content = f.read()

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