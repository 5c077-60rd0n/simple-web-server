"""
This module contains a simple HTTP server that responds to GET requests with a
'Hello, world!' message. It uses the http.server module from the Python 
standard library.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

import logging


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    This class is a simple HTTP request handler that responds to GET requests 
    with a 'Hello, world!' message. It inherits from BaseHTTPRequestHandler 
    provided by the http.server module.
    """

    def do_GET(self):
        """
        This method handles the GET HTTP request. It sends a 200 response 
        status code, sets the content type to 'text/html', ends headers, and 
        sends a 'Hello, world!' message.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n",
                     str(self.path), str(self.headers))


if __name__ == "__main__":
    try:
        PORT = 8000
        server_address = ('', PORT)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

        print(f'Starting httpd on port {PORT}...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.socket.close()
    except Exception as e:
        print(f"Unexpected error: {e}")
