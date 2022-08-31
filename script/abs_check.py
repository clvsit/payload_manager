import abc


class Checker(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractclassmethod
    def check(input_data: dict) -> dict:
        pass
