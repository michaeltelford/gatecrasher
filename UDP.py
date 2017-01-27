
# Network module used for all UDP networking aspects of the Gatecrasher script.
# Developed by Michael Telford.

import socket

# Initializes socket with datagram proto and binds to port arg.
def bind(port):

    global s
    host = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

def send(addr, port):

    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "gatecrasher request"
    address = (addr, port)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    s.sendto(data, address)

def receive(timeout):
    
    global s

    s.settimeout(timeout)
    while 1:
        try:
            string, address = s.recvfrom(1024)
            return True
        except socket.timeout:
            return False

def receive_echo(port):
    
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(('', port))
    # Block until receive and then echo loop (continuous).
    while 1:
        string, address = s.recvfrom(1024)
        s.sendto(string, address)

def close():

    global s
    try:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except socket.error:
        pass

# End of module.

