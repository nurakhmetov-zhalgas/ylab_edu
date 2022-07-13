from itertools import cycle


class CyclicIterator:
    def __init__(self, iter_object):
        self.__iter_object = cycle(iter_object)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__iter_object)
