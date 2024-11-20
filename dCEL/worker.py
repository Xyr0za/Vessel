import requests
import json


class Worker:
    def __init__(self):
        self.identity = ""
        self.rights = {}

    def request_node(self):
        content = json.dumps({"header" : "node"})
        response = requests.post("http://127.0.0.1:5000/rights", data=content)

        response_dict = json.loads(response.text)
        self.identity = response_dict["allocated_identity"]

    def request_rights(self):
        content = json.dumps({"header": "rights", "identity" : f"{self.identity}"})
        response = requests.post("http://127.0.0.1:5000/master", data=content)

        response_dict = json.loads(response.text)
        self.rights = response_dict

    def work(self, function):
        res = []
        initial = self.rights["initial"]
        iters = self.rights["iterations"]
        for i in range(initial, initial + iters):
            res += [
                function(i)
            ]
        print(res)