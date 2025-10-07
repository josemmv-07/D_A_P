class Book:
    def __init__(self, isbn, título, autor, editorial, páginas, precio, ejemplares):
        self.isbn = isbn
        self.título = título
        self.autor = autor
        self.editorial = editorial
        self.páginas = páginas
        
        self.ejemplares = ejemplares
        if precio >= 50 and precio <= 1000:
            self.precio = precio

    def display(self):
        print((self.isbn), (self.título), (self.precio), (self.ejemplares))

    def in_stock(self):
        if self.ejemplares > 0:
            return True
        else:
            return False




book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

books = [book1, book2, book3, book4]

for book in books:
    book.display()

jack = ["Learn Biology", "Learn Chemistry"]


