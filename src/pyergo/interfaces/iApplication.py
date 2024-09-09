from abc import ABC, abstractmethod


class IApplication (ABC):
    @abstractmethod
    def launch(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass
