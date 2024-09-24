import random


class Film:
    def __init__(self, originalTitle, director, genre):
        self.originalTitle = originalTitle
        self.director = director
        self.genre = genre

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
            return NotImplemented

        return self.author == other.author and self.title == other.title

    def __getitem__(self, ind):
        if 0 <= ind < len(self.feedback):
            return self.feedback[ind]
        else:
            return -1


film1 = Film("The Godfather", "Francis Ford Coppola", "Crime, drama")
book1 = Book("Python Crash Course", "Eric Matthes", 624, [random.randint(50, 300) for i in range(12)])

for item in (film1, book1):
    item.show_info()

book2 = Book("JavaScript: The Good Parts", "Douglas Crockford", 170,
             [random.randint(50, 300) for i in range(12)])
book3 = Book("Python Crash Course", "Eric Matthes", 700,
             [random.randint(50, 300) for i in range(12)])

print(book1 == book2)
print(book1 == book3)

print(isinstance(book1, Film))
print(isinstance(book1, Book))

print(book1[2])
