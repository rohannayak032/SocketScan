import socket 
import time

LINE = "─" * 50
TITLE_LINE = "=" * 50

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

def get_valid_port(prompt):
    while True:
        try:
            port = int(input(prompt))

            if not(1 <= port <= 65535):
                print("Port must be in between 1 and 65535")
            
            else:
                return port
        except ValueError:
            print("That's not a valid port!")

def scan_ports(host, start_port, end_port):
    open_count = 0
    print(f"\nScanning {host}...\n")
    print(f"{'PORT':<6}{'SERVICE':<20}STATUS")
    print(LINE)

    for port in range(start_port,end_port+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
            my_socket.settimeout(1)
            result = my_socket.connect_ex((host, port))
            port_name = services.get(port, "Unknown")
            if result == 0:
                status = "OPEN"
                open_count += 1
            else:
                status = "CLOSED"
            print(f"{port:<6}{port_name:<20}{status}")
    return open_count

def print_summary(host, start_port, end_port, scan_time, open_count):
    print(LINE)
    print("Scan Summary")
    print(TITLE_LINE)

    print(f"{'Host':<20}: {host}")
    print(f"{'Ports Scanned':<20}: {end_port - start_port + 1}")
    print(f"{'Open Ports Found':<20}: {open_count}")
    print(f"{'Time Taken':<20}: {scan_time:.2f} s")

    print(TITLE_LINE)

def print_logo():
    print(TITLE_LINE)
    print("SocketScan Port Scanner".center(50))
    print("Version 1.0".center(50))
    print(TITLE_LINE)

def get_valid_host():
    while True:
        host = input("Enter host: ")

        try:
            socket.gethostbyname(host)
            return host

        except socket.gaierror:
            print("\n[ERROR] Unable to resolve host.")
            print("Please enter a valid hostname or IP address.\n")

def main():
    print_logo()

    host = get_valid_host()
    start_port = get_valid_port("Enter start port: ")
    while True:
        end_port = get_valid_port("Enter end port: ")

        if end_port < start_port:
            print("[ERROR] End port cannot be smaller than the start port.\n")
        else:
            break

    start_time = time.time()

    open_count = scan_ports(host, start_port, end_port)

    end_time = time.time()

    scan_time = end_time - start_time

    print_summary(
        host,
        start_port,
        end_port,
        scan_time,
        open_count
    )

if __name__ == "__main__":
    main()









