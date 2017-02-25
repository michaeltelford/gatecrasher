
# Gatecrasher

Gatecrasher in short is a network search tool developed in Python. 

Gatecrasher can be thought of as a subnet broadcast tool which records 
contactable host addresses and displays the IP's to the user.  Different 
protocols and ports can be used to contact potential hosts.

## Usage

`python3` is not supported by Gatecrasher. 

Below is a basic use example:

```shell
git clone https://github.com/michaeltelford/gatecrasher
cd gatecrasher
sudo python gatecrasher.py 192.168.1
```

You may need `root` access to execute the above command. 

### Usage Examples

| Command                                       | Description                   |
| --------------------------------------------- | ----------------------------- |
| python gatecrasher.py 192.168.1               | Pings all hosts on network ID |
| python gatecrasher.py 172.4.208 http          | Checks for all web servers    |
| python gatecrasher.py 10.2.128 ssh 0.7        | Checks for all ssh servers    |
| python gatecrasher.py 82.4.207 @tcp:8080@     | Custom TCP tomcat search      |
| python gatecrasher.py 192.168.0 @udp:67@ 0.05 | Custom UDP network search     |
| python gatecrasher.py echo 8888               | UDP echo server on port 8888  |

3 user arguments can be provided but only 1 is required.  The full 3 args consist 
of a:

- Network ID (required)
- Protocol (optional)
- Timeout (optional interger or float)

Only the network ID is needed meaning the protocol and timeout are taken as the 
default values set by the script which is the 'ICMP' (ping) protocol and 0.25 
second timeout to listen for replies if not provided as arguments.
Greater timeouts may be needed on large networks e.g WAN's for accurate results.

Custom transport layer protocols and port combinations can be used to test
contactable hosts on a given network ID.

Gatecrasher also has a built in UDP echo service which binds to a given port
and echos any data sent to it until interrupted manually by the user (Ctrl+C). 

### Supported Protocols

- ICMP
- HTTP
- HTTPS
- FTP
- FTPS
- SSH
- MySQL

### Notes on Usage

- You may need `root` access to use this application. 
- Gatecrasher was designed and tested on Ubuntu, no other OS's have been
tested but Python is cross platform for the most part
- On IP classes other than class C the network ID is less than needs to be 
provided by Gatecrasher and therefore manual auditing is required for fully 
accurate results

## Thanks

Thanks for looking, feel free to use or fork the repo etc. 

I hope Gatecrasher helps your future network auditing and diagnosis needs. 
