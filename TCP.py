
# Network module used for all TCP networking aspects of the Gatecrasher script.
# Developed by Michael Telford.

import socket

# Initializes socket with stream proto and binds to port arg.
def bind(port):

    global s
    host = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

def connect(addr, port, timeout):

    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (addr, port)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(timeout)
    try:
        s.connect(address)
        close()
        return True
    except (socket.error, socket.timeout):
        return False

def listen(timeout, num_connections):

    global s
    s.settimeout(timeout)
    while 1:
        try:
            s.listen(num_connections)
            conn, addr = s.accept()
            a.append(addr)
        except socket.timeout:
            a.sort()
            return a

def close():

    global s
    try:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except socket.error:
        pass

# End of module.

