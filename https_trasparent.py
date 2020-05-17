from proxy2 import *

class ThreadingHTTPSServer(ThreadingHTTPServer):
    address_family = socket.AF_INET6
    daemon_threads = True

    cakey = 'ca.key'
    cacert = 'ca.crt'

    def get_request(self):
        request, client_address = self.socket.accept()
        request = ssl.wrap_socket(request, keyfile=self.cakey, certfile=self.cacert, server_side=True)
        return request, client_address

    def handle_error(self, request, client_address):
        # surpress socket/ssl related errors
        cls, e = sys.exc_info()[:2]
        if cls is socket.error or cls is ssl.SSLError:
            pass
        else:
            return HTTPServer.handle_error(self, request, client_address)


def test(HandlerClass=ProxyRequestHandler, ServerClass=ThreadingHTTPSServer, protocol="HTTP/1.1"):
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 3129
    server_address = ('', port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTPS Proxy on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()


if __name__ == '__main__':
    test()
