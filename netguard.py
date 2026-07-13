import socket 

for num in range(20,31):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "scanme.nmap.org"
    port = num
    print("Scanning scanme.nmap.org...")
    result = my_socket.connect_ex((host, port))
    if(result != 0):
        print("Port",num,"is CLOSED")
    else:
        print("Port",num,"is OPEN")

    my_socket.close()








