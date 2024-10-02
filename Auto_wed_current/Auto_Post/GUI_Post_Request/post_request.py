import csv

import requests

class post_request():
    def __init__(self, path, execute):
        self.path = path
        self.execute = execute

    def issue_resquest(self, post_combobox):
        for line in post_combobox:
            with open(r'{}\{}'.format(self.path, post_combobox[line]['box_file'].currentText()), 'r', newline='', encoding='utf-8') as f:
                csv_reader = csv.reader(f)
                next(csv_reader)  #
                for row in csv_reader:
                    self.mode_request(row)

    def mode_request(self, request):
        self.execute.af()
        if request[2] == "get":
            r = requests.get(request[3])
            print(r.status_code)

        elif request[2] == "post":
            r = requests.post(request[3])
            print(r.status_code)
        self.execute.bf()