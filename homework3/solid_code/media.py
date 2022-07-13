from abc import ABC, abstractmethod


class AbstractMedia(ABC):
    @abstractmethod
    def notify(self, text):
        pass


class Newspaper(AbstractMedia):
    def notify(self, text):
        print(f"Newspaper news: {text}")
