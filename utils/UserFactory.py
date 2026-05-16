from abc import ABC, abstractmethod

class UserFactory(ABC):

    @abstractmethod
    def create_user(self):
        pass    