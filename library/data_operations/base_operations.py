from abc import ABC, abstractmethod

class BaseOperations(ABC):

    @abstractmethod
    def create_book(self, title, author, year):
        pass

    @abstractmethod
    def read_books(self):
        pass

    @abstractmethod
    def update_book(self, old_title, new_title, new_author, new_year):
        pass

    @abstractmethod
    def delete_book(self, title):
        pass
