from sys import exit


class NoIndexErrorList(list):
    def __init__(self, my_list=[], de=0):
        self.de = int(de)
        self.my_list = my_list
        super(NoIndexErrorList, self).__init__()

    def __getitem__(self, item):
        try:
            return self.my_list[item]
        except IndexError:
            try:
                return self.my_list[self.de]
            except IndexError:
                print('индекс по умолчанию больше длинны списка')
                exit()

    def __repr__(self):
        return str(self.my_list)

    def extend(self, __iterable):
        self.my_list.extend(__iterable)

    def append(self, __object):
        self.my_list.append(__object)

    def pop(self, __index: int = ...):
        return self.my_list.pop(__index)

    def insert(self, __index: int, __object):
        self.my_list.insert(__index, __object)

    def index(self, __value, __start=0, __stop=0):
        __stop = len(self.my_list)
        return self.my_list.index(__value, __start, __stop)

    def count(self, __value):
        return self.my_list.count(__value)

    def sort(self, *, key=None, reverse=False):
        self.my_list.sort(key=key)
        if reverse:
            self.my_list = self.my_list[::-1]
        return self.my_list

    def reverse(self):
        self.my_list = self.my_list[::-1]
        return self.my_list

    def clear(self):
        self.my_list = []
        return self.my_list

    def copy(self):
        return self.my_list.copy()