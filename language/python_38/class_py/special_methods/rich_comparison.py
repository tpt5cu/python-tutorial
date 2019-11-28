# https://docs.python.org/3.8/reference/datamodel.html#object.__lt__
# https://stackoverflow.com/questions/20202418/why-is-the-cmp-parameter-removed-from-sort-sorted-in-python3-0


class Desk:

    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length