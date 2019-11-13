# https://www.afternerd.com/blog/python-http-server/
# https://serverfault.com/questions/78048/whats-the-difference-between-ip-address-0-0-0-0-and-127-0-0-1
# https://forums.tomshardware.com/faq/can-my-computer-have-more-than-one-ip-address.1606720/

import SimpleHTTPServer
import SocketServer

# python -m SimpleHTTPServer 8000

# This file works as is. If it isn't working on Docker, then it's a Docker configuration issue, not a Python issue

# An HTTP web server is a process running on a host that does exactly 2 things:
# 1) It listens for incoming HTTP requests on a specific TCP socket address (which is composed of an IP address and a port number TOGETHER)
#   - The IP address gets the message to the correct machine. It is the interface between the computer and outside
#   - The port number gets the message to the correct process, regardless of which IP address the message came in on
#       - The default port for HTTP is 80 and for HTTPS is 443, so web servers listening on those ports don't need a message to have the port appended
#         to the end of the url
#           - If the webserver is listening on a non-default port, that port must be specified
# 2) It handles the request and sends a response back to the client
#
# Every HTTP message (request or response) always carries a TCP address inside of it. 

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# TCPServer describes a server that uses the TCP protocol to send and receive messages. A TCPServer needs 1) a TCP address and 2) the handler
# - Passing an empty string means the server will listen on ALL available network interfaces (i.e. IP addresses), but only on a single port
# - Passing an IP address means the server will listen ONLY on that IP address and that port
#
# A computer gets 1 IP address for each network interface card (NIC) that is attached to the motherboard
# - A computer can also assign multiple IP address to one NIC, which gives the computer a potentially unlimited number of IP addresses
#   - The more IP addresses are assigned to a single NIC, the greater the risk of a "bottleneck" where the NIC receives a greater rate of data packets
#     than it can handle. When this happens, the NIC will fail to process some packets and network performance will suffer
tcp_address = ("", PORT)
httpd = SocketServer.TCPServer(tcp_address, Handler)
print("serving at port", PORT)
httpd.serve_forever()
# This line never gets printed. Therefore, this code cannot be run directly inside of the Jupyter environment because every cell after this one will
# never execute!!! Need to make a system call.
print("Does this ever get printed?")