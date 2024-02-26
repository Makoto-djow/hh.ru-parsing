from abc import ABC, abstractmethod


class HHAbstract(ABC):

    @abstractmethod
    def get_info(self):
        pass


class AddingVacancies(ABC):
    pass
