import socket
ip = input("What's your IP Address? ")
print("You entered:", ip )
print("\nScanning:", ip )
for port in range(1, 8001):
    print("Scanning port", port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip, port))
if result == 0:
    print("\nPort", port, "is OPEN")
else: print("\nEvery port is closed.")
sock.close()