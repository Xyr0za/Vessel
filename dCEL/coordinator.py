class Coordinator:
    def __init__(self, current_iter = 0, batch_size = 1000, nodes = {}):
        self.current_iter = current_iter
        self.batch_size = batch_size
        self.nodes = nodes

    def generate_response(self, identity):
        return {"ID" : identity, "initial" : self.current_iter, "iterations" : self.batch_size}#

    def verify(self, data):
        if data["header"] == 'rights':
            if data["identity"] in self.nodes:
                return True
        return False

    def add_node(self, addition):
        self.nodes.add(addition)