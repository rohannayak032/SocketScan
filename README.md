# SocketScan - TCP Port Scanner

A lightweight TCP port scanner written in Python using the socket module. It supports configurable host and port ranges, service detection, and a clean command-line interface.

## Disclaimer

This project was developed for educational purposes to learn Python socket programming and networking concepts. Only scan hosts and networks that you own or have explicit permission to test.

## Features

- Scan any hostname or IP address
- Custom port range
- Input validation
- Common service detection
- Scan timing
- Scan summary
- Clean CLI interface

## Technologies Used

- Python 3
- socket
- time

## Installation

Clone the repository:

```bash
git clone https://github.com/rohannayak032/SocketScan.git
```

Run:

```bash
python socketscan.py
```

## Example

```text
==================================================
              SocketScan Port Scanner
                   Version 1.0
==================================================

Scanning scanme.nmap.org...

PORT   SERVICE              STATUS
────────────────────────────────────────
22     SSH                  OPEN
80     HTTP                 OPEN
443    HTTPS                OPEN

Scan Summary
==================================================
Host              : scanme.nmap.org
Ports Scanned     : 1024
Open Ports Found  : 3
Time Taken        : 0.52 s
==================================================
```

## Author

Built by Rohan Nayak as a cybersecurity learning project.