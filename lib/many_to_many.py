class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []

        Author.all.append(self)
    
    def contracts(self):
        return self._contracts
    
    def books(self):
        return self._books
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        royalties = [contract.royalties for contract in self._contracts]
        return sum(royalties)

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []

        Book.all.append(self)
    
    def contracts(self):
        return self._contracts
    
    def authors(self):
        return self._authors

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        self.author._contracts.append(self)
        self.author._books.append(self.book)

        self.book._contracts.append(self)
        self.book._authors.append(self.author)

        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception("Author must be instance of Author")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception("Book must be instance of Book")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        if type(new_date) == str:
            self._date = new_date
        else:
            raise Exception("Date must be a string")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, new_royalties):
        if type(new_royalties) == int:
            self._royalties = new_royalties
        else:
            raise Exception("Royalties must be a number")
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
    def __str__(self):
        return f"Author: {self.author}. Book: {self.book}. Date: {self.date}. Royalties: {self.royalties}."

author1 = Author("Name 1")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
author2 = Author("Name 2")
book4 = Book("Title 4")
contract1 = Contract(author1, book1, "02/01/2001", 10)
contract2 = Contract(author1, book2, "01/01/2001", 20)
contract3 = Contract(author1, book3, "03/01/2001", 30)
contract4 = Contract(author2, book4, "01/01/2001", 40)
print(Contract.contracts_by_date('01/01/2001'))