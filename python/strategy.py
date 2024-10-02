from abc import ABC, abstractmethod


# Base strategy class
class Strategy(ABC):
    def __init__(self, input=None, dictionary=None):
        self.input = input
        self.dictionary = dictionary

    @abstractmethod
    def translate(self):
        pass
