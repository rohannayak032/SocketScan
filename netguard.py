import socket 

services = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS-NS",
    138: "NetBIOS-DGM",
    139: "NetBIOS-SSN",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle DB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alternate"
}
host = input("Enter host: ")
while True:
    try:
        start_port = int(input("Enter start port: "))
        if 1<= start_port <= 65535:
            break
        else:
            print("Port must be between 1 and 65535")
    except ValueError:
        print("That's not a valid port!")
while True:
    try:
        end_port = int(input("Enter end port: "))
        if not (1<=end_port<=65535):
            print("Port should be between 1 and 65535")
        elif (start_port>end_port):
            print("Start port cannot be greater in value than end port")
        else:
            break
    except ValueError:
        print("That's not a valid port!")

print(f"Scanning {host}...")
open_count = 0
print("PORT SERVICE STATUS")
print("-------------------------")
for port in range(start_port,end_port+1):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = my_socket.connect_ex((host, port))
    port_name = services.get(port,"Unknown")
    if(result != 0):
        status = "CLOSED"
    else:
        status = "OPEN"
        open_count+=1
    print(f"{port:<6}{port_name:<20}{status}")

    my_socket.close()








