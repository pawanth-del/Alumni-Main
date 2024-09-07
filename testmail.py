import socket

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

print(is_port_open('smtp.gmail.com', 587))  # Check for TLS port
print(is_port_open('smtp.gmail.com', 465))  # Check for SSL port