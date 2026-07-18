import socket 
import time
from concurrent.futures import ThreadPoolExecutor

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

def scan_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
        my_socket.settimeout(1)
        result = my_socket.connect_ex((host,port))
        port_name = services.get(port,"Unknown")
        return {
            "port":port,
            "open": result == 0,
            "status": "OPEN" if result == 0 else "CLOSED",
            "service": port_name
        }

def scan_ports(host, start_port, end_port):
    results = []
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []

        for port in range(start_port, end_port + 1):
            future = executor.submit(scan_port, host, port)
            futures.append(future)
        for future in futures:
            port_info = future.result()
            if port_info["open"]:
                results.append(port_info)
    scan_time = time.time() - start_time
    scan_data = {
        "host": host,
        "ports": results,
        "scan_time": scan_time,
        "threads":100,
        "total_ports": end_port-start_port+1,
        "open_ports": len(results)
    }
    return scan_data

def print_report(scan_data):
    print(TITLE_LINE)
    print("SocketScan Report".center(50))
    print(TITLE_LINE)

    print(f"Host: {scan_data['host']}")

    print(TITLE_LINE)
    print("Open Ports")
    print(LINE)

    if not scan_data["ports"]:
        print("No open ports found.")
    else:
        print(f"{'PORT':<8}{'STATUS':<10}SERVICE")
        print(LINE)
        for port in scan_data["ports"]:
            print(f"{port['port']:<8}{port['status']:<10}{port['service']}")
    print(LINE)

    print(f"{'Ports Scanned':<20}: {scan_data['total_ports']}")
    print(f"{'Open Ports Found':<20}: {scan_data['open_ports']}")
    print(f"{'Threads Used':<20}: {scan_data['threads']}")
    print(f"{'Scan Time':<20}: {scan_data['scan_time']:.2f} s")

    print(TITLE_LINE)

def print_logo():
    print(TITLE_LINE)
    print("SocketScan Port Scanner".center(50))
    print("Version 1.1.0".center(50))
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

    scan_data = scan_ports(host, start_port, end_port)

    print_report(scan_data)

if __name__ == "__main__":
    main()









