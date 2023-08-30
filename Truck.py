from HashMap import HashMap


class Truck:

    def __init__(self):
        self.packages = HashMap()

    def load(self, package):
        self.packages.insert(package[0], package)