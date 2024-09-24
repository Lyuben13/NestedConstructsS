
import random
class Film:
    def __init__(self, originalTitle, director, genre):
        self.originalTitle: str = originalTitle
        self.director: str = director
        self.genre: int = genre

    def show_info(self):
        print(f"Original title: {self.originalTitle}")
        print(f"Director: {self.director}")
        print(f"Genre: {self.genre}")


class Book:
    def __init__(self, title, author, pages, feedback):
        self.title = title
        self.author = author
        self.pages = pages
        self.feedback = feedback
    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, pages: {self.pages}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return 'Not implemented'

        if self.author == other.author and self.title == other.title:
            return True
        else:
            return False

    def __getitem__(self, ind):
        if 0 <= ind <= 11:
            return self.feedback[ind]
        else:
            return -1

film1 = Film("The Godfather", "Francis Ford Coppola", "Crime, drama")
book1 = Book("Python Crash Course", "Eric Matthes", 624)
for item in (film1, book1):
    item.show_info()
book1 = Book("Python Crash Course", "Eric Matthes", 624)
book2 = Book("JavaScript: The Good Parts", "Douglas Crockford", 170)
book3 = Book("Python Crash Course", "Eric Matthes", 700)
print(book1 == book2)  #False
PythonFeedbacks = [random.randint(50, 300) for i in range(12)]
print(isinstance(Book, Film))
print(book1 == book3)
# print(book1 > book2)
print(book1 == film1)
print(book1[2]) #265
