import socket
import threading
import json

class SlowAPI:
    def __init__(self):
        # self.host = socket.gethostbyname("localhost")
        self.host = "192.168.0.127"
        self.port = 5671
        self.cors = False
        self.routes = {}
    
    def route(self, path, method):
        # print("Here we are now")
        def wrapper(function):
            self.routes[(path, method)] = function
            return function
        return wrapper

    def parse_request(self, request):
        req = {}
        lines = request.split("\r\n")
        # print(lines)

        method, urlandquery, http_version = lines[0].split(" ")
        # print(method, urlandquery, http_version)
        
        if '?' in urlandquery:
            url, queries = urlandquery.split("?")
        else:
            url = urlandquery
            queries = ""
        query = {}
        headers = {}
        for q in queries.split("&"):
            if "=" not in q:
                continue
            var, val = q.split("=")
            query[var] = val

        for line in lines[1: -2]:
            if line == "" or ": " not in line:
                continue
            name, value = line.split(": ")
            headers[name] = value
        try:
            body = json.loads(lines[-1])
        except Exception:
            body = {}
        req = {
            "http": http_version,
            "method": method,
            "url": url,
            "query": query,
            "headers": headers,
            "body": body
        }
        # print(req)
        return req
    
    def handle_request(self, client_socket):
        try:
            request = client_socket.recv(25000000).decode()
            # print(f"Received request:\n{request}\n")
            req = self.parse_request(request)

            path = req["url"]
            method = req["method"]

            handler_function = self.routes.get((path, method))
            # print(self.routes)
            if handler_function:
                status, body = handler_function(req)
                response = self.create_response(req, status, body)
            else:
                response = self.create_response(req, 400, {"message": self.get_status_name(400)})

            client_socket.sendall(response)

        except Exception as err:
            print(f"Error handling request: {err}\n")
        finally:
            client_socket.close()

    def get_status_name(self, status_code):
        status_codes = {
            100: "Continue",
            101: "Switching Protocols",
            200: "OK",
            201: "Created",
            204: "No Content",
            301: "Moved Permanently",
            302: "Found",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error",
            503: "Service Unavailable"
        }
        return status_codes.get(status_code, "Unknown Status")

    def create_response(self, req, status, body):
        reqBody = ""
        reqbinBody = b""
        isbin = False
        if req["method"] == "OPTIONS":
            headers = "HTTP/1.1 200 OK\r\n"
            headers += "Content-Length: 0\r\n"
            if self.cors:
                headers += f'Access-Control-Allow-Origin: {req["headers"]["Origin"]}\r\n'
                headers += 'Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS\r\n'
                headers += 'Access-Control-Allow-Credentials: true\r\n'
                headers += 'Access-Control-Allow-Headers: Content-Type\r\n'
                headers += 'Access-Control-Max-Age: 86400\r\n'
        else:
            headers = f"HTTP/1.1 {status} {self.get_status_name(status)}\r\n"
            if isinstance(body, dict):
                if "isbin" in body:
                    content_type = body["mimetype"] + "\r\n" + str(body["content-length"])
                    reqbinBody += body["file"]
                    isbin = True
                else:
                    reqBody = json.dumps(body)
                    content_type = "application/json"
            elif isinstance(body, str):
                reqBody = body
                content_type = "text/plain"
            else:
                reqBody = ""
                content_type = "text/plain"
            
            headers += f"Content-type: {content_type}" + "\r\n"
            if self.cors:
                if "Origin" in req["headers"]:
                    headers += f'Access-Control-Allow-Origin: {req["headers"]["Origin"]}\r\n'
                headers += 'Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS\r\n'
                headers += 'Access-Control-Allow-Credentials: true\r\n'
                headers += 'Access-Control-Allow-Headers: Content-Type\r\n'
                headers += 'Access-Control-Max-Age: 86400\r\n'
        headers += '\r\n'

        if isbin:
            # print("initiating")
            # print(headers)
            response = headers.encode() + reqbinBody
            # print("done")
            return response
        
        else:
            response = headers + reqBody
            # print("Non bytes", response)
            return response.encode()
    
    def listen(self, port=5671, cors=False):
        self.port = port
        self.cors = cors
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 25000000)
        server_socket.bind((self.host, self.port))
        server_socket.listen()

        print(f"SlowAPI server running on: http://{self.host}:{self.port}")

        while True:
            # print("Waiting for a connection...\n")
            client_socket, client_address = server_socket.accept()
            # print(f"Accepted connection from: {client_socket}\n")

            client_thread = threading.Thread(target=self.handle_request, args=(client_socket,))
            client_thread.start()
