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

print("Scanning scanme.nmap.org...")
for num in range(20,31):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "scanme.nmap.org"
    port = num
    result = my_socket.connect_ex((host, port))
    port_name = services.get(num,"Unknown")
    if(result != 0):
        print(num,port_name,"CLOSED")
    else:
        print(num, port_name,"OPEN")

    my_socket.close()








