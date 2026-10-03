import socket
socket.setdefaulttimeout(1)
print("=====Port Scanner=====")

target = input("Enter the target IP address :").strip()


port = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]

print("\nScanning target : ", target)

for port in port:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((target, port))
    if result == 0:
        print("Port" , port, "is OPEN")
    else:
        print("Port" , port, "is CLOSED")
    sock.close()

    print("\nScanning completed")