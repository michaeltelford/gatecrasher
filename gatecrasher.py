
# Gatecrasher script to find 'awake' hosts running different protocol services.
# Developed by Michael Telford.

import socket, sys, time           # Standard modules
import UDP, TCP, ICMP              # Created modules

# Check user privilages for ping functionality.
def check_ping_priv():
    try:
        ICMP.ping("localhost", 0.01)
    except socket.error:
        print("Must have root (administrator) privilages for ICMP, Goodbye")
        sys.exit(0)

# Ping hosts on network using the network ID arg.
def ping(netid, tout):
    i = 1
    a = []

    check_ping_priv()

    print("Pinging hosts now, remember that patience is a virtue...")
    try:
        stime = time.time()
        while i < 255:
            host = netid + "." + str(i)
            if ICMP.ping(host, tout):
                a.append(host)
            i += 1
        etime = time.time()
        duration = etime - stime
    except socket.error:
        print("A socket error has occured, exiting")
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

    # Print awake hosts, if any.
    print("Tests took " + str(int(duration)) + " seconds with a " + str(tout) + " timeout")
    if len(a) > 0:
        print("The following hosts are 'awake' : ")
        # Do not sort array, it's already done due to i var being incremented.
        for x in a:
            print(x)
    else:
        print("No hosts are awake or they're just not responding to ICMP ping requests")

# Check for servers running TCP based software such as HTTP and HTTPS etc...
def tcp_conn(netid, port, tout):
    global proto
    i = 1
    a = []

    print("Gathering host IP's now, remember that patience is a virtue...")
    try:
        stime = time.time()
        while i < 255:
            host = netid + "." + str(i)
            if TCP.connect(host, port, tout):
                a.append(host)
            i += 1
        etime = time.time()
        duration = etime - stime
    except socket.error:
        print("A socket error has occured, exiting")
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

    # Print awake hosts, if any.
    print("Tests took " + str(int(duration)) + " seconds with a " + str(tout) + " timeout")
    if len(a) > 0:
        print("The following hosts are running " + proto +  " server software :")
        # Do not sort array, it's already done due to i var being incremented.
        for x in a:
            print(x)
    else:
        print("No hosts are awake or they're just not responding to " + proto + " requests")

def udp_send_receive(netid, port, tout):
    i = 1
    a = []

    print("Gathering host IP's now, remember that patience is a virtue...")
    try:
        stime = time.time()
        while i < 255:
            host = netid + "." + str(i)
            UDP.send(host, port)
            if UDP.receive(tout):
                a.append(host)
            i += 1
        etime = time.time()
        duration = etime - stime
    except socket.error:
        print("A socket error has occured, exiting")
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

    # Print awake hosts, if any.
    print("Tests took " + str(int(duration)) + " seconds with a " + str(tout) + " timeout")
    if len(a) > 0:
        print("The following hosts responded to the UDP packet sent :")
        # Do not sort array, it's already done due to i var being incremented.
        for x in a:
            print(x)
    else:
        print("No hosts are awake or they're just not responding to UDP packets")

def raw_data(netid, proto, tout):
    # Obtain the correct protocol and port
    p = proto
    port = p[p.find(":")+1 : p.find("#")]
    proto = p[p.find("@")+1 : p.find(":")]
    
    # Perform raw data transmissions
    if proto == "tcp" or proto == "TCP":
        tcp_conn(netid, int(port), tout)
    elif proto == "udp" or proto == "UDP":
        udp_send_receive(netid, int(port), tout)
    else:
        print("Incorrect argument usage, see help below")
        print_help()
        sys.exit(0)

# Prints usage help to user if incorrect num of args is provided.
def print_help():
    print("""
Gatecrasher can be thought of as a subnet broadcast tool which records 
contactable host addresses and displays them to the user.  Different protocols
and ports can be used to contact potential hosts.

3 user arguments can be provided but only 1 is needed.  The full 3 args consist 
of a network ID string, a protocol or service string, and lastly a timeout 
integer or floating point integer for connections and replies depending on
the nature of the selected service.
Only the network ID is needed meaning the protocol and timeout are taken as the 
default values set by the script which is the 'ICMP' (ping) protocol and 0.25 
second timeout to listen for replies if not provided as arguments.
Greater timeouts may be needed on WAN's for accurate results.

Custom transport layer protocols and port combinations can be used to test
contactable hosts on a given network ID.
Gatecrasher also has a built in UDP echo service which binds to a given port
and echos any data sent to it until interrupted by the user manually.
See usage examples below.

NOTES FOR USE : 

1) Gatecrasher was designed and tested on Ubuntu, no other OS's have been
tested but Python is cross platform for the most part.
2) On IP classes other than class C the network ID is less than needs to be 
provided by Gatecrasher and therefore manual auditing is required for fully 
accurate results.

Usage examples :

gatecrasher.py 192.168.1                - Pings all hosts on network ID
gatecrasher.py 172.4.208 http           - Checks for all web servers
gatecrasher.py 10.2.128 ssh 0.7         - Checks for all ssh servers
gatecrasher.py 82.4.207 @tcp:8080@      - Custom TCP tomcat search
gatecrasher.py 192.168.0 @udp:67@ 0.05  - Custom UDP network search
gatecrasher.py echo 8888                - UDP echo server on port 8888

Standard supported protocols include :
ICMP, HTTP, HTTPS, FTP, FTPS, SSH, MySQL

Hope Gatecrasher helps you with your future network auditing and diagnosis.
Developed by Michael Telford (.)(.) \n""")

def main():
	# Default variables if not set via user args.
	netid = None
	proto = 'ICMP'
	tout = 0.25
	
	# User arguments.
	if len(sys.argv) == 2:
		if sys.argv[1] == '-h' or sys.argv[1] == '-help' or sys.argv[1] == '--help':
			print_help()
			sys.exit(0)
		else:
			netid = sys.argv[1]
	elif len(sys.argv) == 3:
		if sys.argv[1] == "echo" or sys.argv[1] == "ECHO":
			print("Echoing UDP data now...")
			try:
				UDP.receive_echo(int(sys.argv[2]))
			except KeyboardInterrupt:
				sys.exit(0)
			except socket.error:
				print("Socket error, check user permissions")
				sys.exit(0)
		else:
			netid = sys.argv[1]
			proto = sys.argv[2]
	elif len(sys.argv) == 4:
		netid = sys.argv[1]
		proto = sys.argv[2]
		tout = float(sys.argv[3])
	else:
		print("Incorrect argument usage, see help below")
		print_help()
		sys.exit(0)
	
	# Perform network search for hosts on given protocol/service.
	if proto == 'icmp' or proto == 'ICMP' or proto == 'ping':
		ping(netid, tout)
	elif proto == 'http' or proto == 'HTTP':
		tcp_conn(netid, 80, tout)
	elif proto == 'https' or proto == 'HTTPS':
		tcp_conn(netid, 443, tout)
	elif proto == 'ftp' or proto == 'FTP':
		tcp_conn(netid, 21, tout)
	elif proto == 'ftps' or proto == 'FTPS':
		tcp_conn(netid, 990, tout)
	elif proto == 'ssh' or proto == 'SSH':
		tcp_conn(netid, 22, tout)
	elif proto == 'mysql' or proto == 'MYSQL' or proto == 'MySQL':
		tcp_conn(netid, 3306, tout)
	elif proto.find("@") != -1:
		raw_data(netid, proto, tout)
	else:
		print("Incorrect argument usage, see help below")
		print_help()
		sys.exit()
	
	#raw_input("Press any key to exit...")
	exit(1)

if __name__ == '__main__':
    main()
