import csv

import requests

class post_request():
    def __init__(self, path, execute):
        self.path = path
        self.execute = execute

    def issue_resquest(self):
        with open(self.path, 'r', newline='', encoding='gbk') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # 跳过第一行
            for row in csv_reader:
                self.mode_request(row)

    def mode_request(self, request):
        self.execute.af()
        if request[2] == "get":
            r = requests.get(request[3])
            print(r.status_code)

        elif request[2] == "post":
            requests.post(request[3])
        self.execute.bf()