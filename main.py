import datetime


class fruit_tree:                                                           # create class
    __YEAR, __HEIGHT, __BRANCHES, __DATE_START = 1, 0.1, 3, 2000            # start value

    __slots__ = ["__year", "__height", "__branches", "__date_now", "__date_start"]    #limitation instaces

    def __init__(self):
        self.__year = fruit_tree.__YEAR
        self.__height = fruit_tree.__HEIGHT
        self.__branches = fruit_tree.__BRANCHES
        self.__date_start = fruit_tree.__DATE_START
        self.__date_now = datetime.date.today().year

    def info(self):                                                                   # return values instaces
        return self.__year, self.__height, self.__branches

    def grow(self, year, height, branch):                                             # method grow
        self.__year = self.__year + year
        self.__height = self.__height + height
        self.__branches = self.__branches + branch

    def time_live(self):                                                               #determine the number of iterations, iterate and passing magnification values
        while self.__date_start <= self.__date_now:
            self.__date_start = self.__date_start + 1
            x.grow(1, 1.5, 3)
            print(f"Через год: {x.info()}")


x = fruit_tree()                                                                       #redefining the class into a variable for subsequent calls to methods of this class
print(f"В первый год: {x.info()}")                                                     #print start values
x.time_live()
