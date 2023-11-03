class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return "Pair(" + str(self.first) + "," + str(self.second) + ")"
