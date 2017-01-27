
# Gatecrasher

Gatecrasher in short is a network search tool developed in Python. 

Gatecrasher can be thought of as a subnet broadcast tool which records 
contactable host addresses and displays them to the user.  Different protocols
and ports can be used to contact potential hosts.

## Usage

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

## Thanks

Thanks for looking, feel free to use or fork the repo etc. 

I hope Gatecrasher helps your your future network auditing and diagnosis needs. 
