# -*- coding: utf-8 -*-
from proxy2 import *

class UAChangerRequestHandler(ProxyRequestHandler):
    def request_handler(self, req, req_body):
        req.headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.01; Windows 98)'


if __name__ == '__main__':
    test(HandlerClass=UAChangerRequestHandler)
