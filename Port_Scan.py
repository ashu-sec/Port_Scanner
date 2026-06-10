import sys
import socket
from datetime import datetime


Target = input("Enter IP address, Domain, URL: ")
Start_port = int(input("Enter Starting Port: "))
End_port = int(input("Enter Ending Port: "))



try:
    Target_IP = socket.gethostbyname(Target)
    print()
    print("Domain Name: ", Target)
    print("Target IP: ", Target_IP) 

except socket.gaierror:
    print("Enter valid IP, Domain, URL...")
    sys.exit()



if (Start_port > End_port):
    print("Error: Starting point cannot greater than ending port.")
    sys.exit()

if(Start_port < 1 or End_port > 65535):
    print("Error: Invalid Port Number.")
    sys.exit()
Start_time = datetime.now()



print()
print("----------------------------------------")
print("Simple Port Scanner...")
print()
print("Target: ", Target_IP)
print("Ports: ", Start_port,"-", End_port)
print("Start_time:", Start_time.strftime("%H:%M:%S"))
print("----------------------------------------")
print()



Open_ports = []
for port in range(Start_port,End_port+1):
    print("Checking port...", port, end="\r")
    sys.stdout.flush()
    
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.settimeout(1.0)
    result = connection.connect_ex((Target_IP, port))
    if (result==0):
        print("Port", port, "is open")
        Open_ports.append(port)
    connection.close()
End_time = datetime.now()



print()
print("--------------------------")
print(" Summary")
print("--------------------------")



if (Open_ports == []):
    print("No open port found")
else:
    print("Open ports are ", Open_ports)

print("Finished: ", End_time.strftime("%H:%M:%S"))