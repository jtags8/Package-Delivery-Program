from HashMap import HashMap


class Truck:

    def __init__(self):
        self.packages = []

    def load(self, package):
        self.packages.append(package)