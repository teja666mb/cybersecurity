import socket

target = input("Enter Target IP or Domain: ")

ports = [21, 22, 23, 25, 53, 80, 110, 443]

report = []

print("\nScanning...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        report.append(f"Port {port}: OPEN")
    else:
        print(f"Port {port} is CLOSED")
        report.append(f"Port {port}: CLOSED")

    sock.close()

with open("vulnerability_report.txt", "w") as file:
    file.write("VULNERABILITY SCAN REPORT\n")
    file.write("=========================\n")
    file.write(f"Target: {target}\n\n")

    for item in report:
        file.write(item + "\n")

print("\nReport generated: vulnerability_report.txt")