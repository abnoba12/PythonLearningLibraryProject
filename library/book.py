class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def update(self, title=None, author=None, year=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year

    def display(self):
        print(f"{self.title} by {self.author} ({self.year})")
