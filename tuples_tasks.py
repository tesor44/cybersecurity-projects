import socket
class Infiltrator:
    def __init__(self, ip):
        self.target_ip = ip
        self.open_ports = []
    def scan_range(self, start, end):
        for i in range(start, end):
            sock = socket.socket()
            sock.settimeout(0.5)
            try:
                sock.connect((self.target_ip, i))
                self.open_ports.append(i)  
            except:
                pass
            sock.close()
    def report(self):
        print(self.open_ports)
scanner = Infiltrator("127.0.0.1")
scanner.scan_range(130, 140)
scanner.report()

        