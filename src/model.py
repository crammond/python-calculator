from functions import Number


class Model:

    def __init__(self):
        self.values = []
        self.reset_values()

    def reset_values(self):
        self.values = [Number(0)]

    def index(self):
        return len(self.values) - 1

    def current(self, value=None):
        if value is None:
            return self.values[self.index()]

        self.values[self.index()] = value

