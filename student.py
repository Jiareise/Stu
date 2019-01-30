class Student:
    __counts = 0
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score
        self.__count()
    @classmethod
    def __count(cls):
        cls.__counts += 1
        return cls.__counts
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_score(self):
        return self.__score
    def set_age(self, value):
        self.__age = value
    def set_score(self, value):
        self.__score = value