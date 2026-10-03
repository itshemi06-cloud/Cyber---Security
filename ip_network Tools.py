import socket
import ipaddress

print("=====IP Network Tools=====")

while True:
    print("\n1.Check IP Address")
    print("2.Find Hostname")
    print("3.Find IP Address")
    print("4.exit")
    choice = input("Enter your choice : ")

    if choice == '1':
        ip = input("Enter the IP address : ")
       
        try:
            ipaddress.ip_address(ip)
            print("valid IP address !.")
        except ValueError:
            print("Invalid IP address.")

    elif choice == '2':
        ip = input("Enter the IP address : ")
        try:
            hostname = socket.gethostbyaddr(ip)
            print("Hostname : ", hostname[0])
        except socket.herror:
            print("Hostname : Not found.")

    elif choice == '3':
        
        hostname = input("Enter the hostname : ")
        try:
            ip = socket.gethostbyname(hostname)
            print("IP Address : ", ip)
        except socket.gaierror:
            print("IP Address : Not found.")

    elif choice == '4':


        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")