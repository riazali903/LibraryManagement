
class Book:
    books = []
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.books.append(self)

class Member:
    members = []
    def __init__(self,name, member_id):
        self.name = name
        self.member_id = member_id
        self.members.append(self)

class Library(Member,Book):
    def __init__(self,name,member_id):
        Member.__init__(self,name,member_id)
        self.books = []
        self.members = []

    def add_book(self):
        for book in Book.books:
            self.books.append(book)


    def display_books(self):
        for i in self.books:
            print(f'{i.title}, {i.author}')

    def add_member(self):
        for member in Member.members:
            self.members.append(member)

    def display_members(self):
        for member in self.members:
            print(f'{member.name}, {member.member_id}')


    def checkout_book(self,member_id,book_isbn):
        print(f'{member_id} barrrowed {book_isbn}')
        for book in self.books:
            if book.isbn == book_isbn:
                self.books.remove(book)

print(Library.__mro__)
mem = Member('Riaz','900')
b1 = Book('Atomic Habits','Koemne','IS2345223')
b2 = Book('Good', 'Ali','isbn-----')

lib = Library('Ali',500)
lib.add_book()
lib.display_books()
lib.checkout_book('900','IS2345223')
print('end')
lib.display_books()



