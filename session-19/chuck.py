import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINTS = ("/jokes", "/categories", "/jokes/random")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used

RESULTS=[]

for ENDPOINT in ENDPOINTS:
    conn = http.client.HTTPConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Generate the object from the json file
    result = json.loads(text_json)

    #generating all the jokes
    data= result['value']
    RESULTS.append(data)




jokes= RESULTS[0]
categories=RESULTS[1]
random=RESULTS[2]
#calculating the number of jokes that

countjokes= len(jokes)

#calculating the number of categories

countcategories=len(categories)

#generating random joke


#PRINTING RESULTS:
print('\n\n>The number of total jokes is: ', countjokes)
print('\n>The number of total categories is :', countcategories)
print('\n>The available categories are :', categories)
print('\n>Here you have a random joke :\n    -', random['joke'])
