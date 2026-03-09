import socket
class PortScanner:
    def __init__(self, ip):
        self.target = ip
    def scan(self, port):
        sock = socket.socket()
        sock.settimeout(0.5)
        try:
            sock.connect((self.target , port))
            print("Порт открыт!")
        except:
            print("Порт закрыт...")
            sock.close()
my_scan = PortScanner("127.0.0.1")
ports = [21, 22, 80, 443, 3306]
for i in ports:
    my_scan.scan(i)