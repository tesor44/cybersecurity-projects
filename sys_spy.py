import os, sys
class SysSpy:
    def __init__(self, filename):
        self.report = filename
    def get_info(self):
        info = [os.getcwd(), os.getlogin(), sys.platform]
        return info
    def save(self, data_list):
        with open(self.report, "a") as f:
            for i in data_list:
                f.write(i + "\n")
spy = SysSpy("report.txt")
data = spy.get_info()
spy.save(data)

print("Отчет 'report.txt' готов!")