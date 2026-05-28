import socket

print("===== TCP PORT SCANNER =====")

target = input("Enter target IP or website: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else :
        print(f"Port {port} is closed")
    scanner.close()

print("\nScan Completed!")