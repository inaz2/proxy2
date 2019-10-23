# proxy2

HTTP/HTTPS proxy in a single python script


## Features

* easy to customize
* require no external modules
* support both of IPv4 and IPv6
* support HTTP/1.1 Persistent Connection
* support dynamic certificate generation for HTTPS intercept
* all openssl operations does via pyopenssl api without any syscalls
* support certificate generation with subjectAltName extension for prevent ERR_CERT_COMMON_NAME_INVALID error.

This script works on Python 2.7.
You need to install OpenSSL to intercept HTTPS connections.


## Usage

Just run as a script:

```
$ python proxy2.py
```

Above command runs the proxy on localhost:8080.
Verify it works by typing the below command on another terminal of the same host.

```
$ http_proxy=localhost:8080 curl http://www.example.com/
```

proxy2 is made for debugging/testing, so it only accepts connections from localhost.

To use another port, specify the port number as the first argument.

```
$ python proxy2.py 3128
```


## Enable HTTPS intercept

This proxy intercepts HTTPS connections automatically. It generates private keys and a private CA certificate during 
the first run or if it doesn't exist as ca.crt, cert.key and ca.key at ssl-data folder. You may change it names at ssl_wrapper.py
file.

Through the proxy, you can access http://proxy2.test/ and install the CA certificate in the browsers.


## Customization

You can easily customize the proxy and modify the requests/responses or save something to the files.
The ProxyRequestHandler class has 3 methods to customize:

* request_handler: called before accessing the upstream server
* response_handler: called before responding to the client
* save_handler: called after responding to the client with the exclusive lock, so you can safely write out to the terminal or the file system

By default, only save_handler is implemented which outputs HTTP(S) headers and some useful data to the standard output.
