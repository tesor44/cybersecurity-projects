import socket
import threading
import time
class Infiltrator:
    def __init__(self, ip):
        self.open_port = []
        self.target_ip = ip
    def scan_port(self, port):
        self.ports = port
        sock = socket.socket()
        sock.settimeout(0.5)
        try:
            sock.connect((self.target_ip, port))
            self.open_port.append(port)
            sock.close()
        except:
            pass
    def fast_scan(self, start ,end):
        for i in range(start, end + 1):
            t = threading.Thread(target=self.scan_port, args=(i,))
            t.start()
    def save_to_file(self):
        with open("report.txt" , "w") as f:
            f.write("Отчет для " + self.target_ip + "\n")
            for p in self.open_port:
                f.write("[+] Порт: " + str(p) + "\n")
    def report (self):
        print("---ОТЧЕТ ПО ЦЕЛИ " + self.target_ip + "----")
        for n in self.open_port:
            print("[+] Открытый порт: " + str(n))
scanner = Infiltrator("127.0.0.1")
scanner.fast_scan(1, 500)
time.sleep(2)
scanner.report()
scanner.save_to_file()