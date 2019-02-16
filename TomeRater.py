import sys
print(sys.version)
class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        print("Creating user: {}".format(self.name))
        self = name
    def get_email(self):
        return self.email
    def change_email(self, address):
        self.email = address
        print("New email address: {}".format(address))
    def __repr__(self):
        return("User: \"{}\", email: \"{}\", books read: {}".format(self.name, self.email, self.books))
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
    def read_book(self, book, rating=None):
        self.books[book] = rating
    def get_average_rating(self):
        total = 0
        n = 0
        if len(self.books) > 0:
            for rating in self.books.values():
                if rating:
                    total += rating
                    n += 1
                else:
                    continue
        if n > 0:
            return total/n
        else:
            print("There are no books with ratings for {user}".format(user=self.name))

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        #Tome_Rater.books[title] = 0
        print("Creating book {}".format(title))
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's isbn has been updated to {}".format(self.isbn))
    def add_rating(self, rating):
        if rating:
            if rating <=4 and rating >= 0:
                self.ratings.append(rating)
                print("Rating of {} added.".format(rating))
            else:
                print("Invalid Rating")
    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn
    def get_average_rating(self):
        averagecounter = 0
        for rating in self.ratings:
            averagecounter += rating
        return averagecounter / len(self.ratings)
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __repr__(self):
        return self.title

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        print("Initializing TomeRater...")
    def create_book(self, title, isbn):
        newbook = Book(title, isbn)
        self.books[newbook] = 0
        return newbook
    def __repr__(self):
        return ("TOME RATER, a tool to help organize books, readers and ratings.\n This instance of Tome Rater contains users: {}\n with books {}".format(self.users, self.books))
    def __eq__(self,other):
        if self.users == other.users and self.books == other.books:
            return True
        else:
            return False
    def create_novel(self, title, author, isbn):
        newfiction = Fiction(title, author, isbn)
        self.books[newfiction] = 0
        return newfiction
    def create_non_fiction(self, title, subject, level,isbn):
        newnontifction = Non_fiction(title, subject, level, isbn)
        self.books[newnontifction] = 0
        return newnontifction
    def add_book_to_user(self, book, email, rating=None):
        username = self.users.get(email, None)
        if username:
            username.read_book(book, rating)
            book.add_rating(rating)
            self.books[book] = self.books.get(book, 0) + 1
        else:
            print("No user with email {}".format(email))
    def add_user(self, name, email, user_books=None):
        new_user = User(name,email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book,email)
    def print_catalog(self):
        for key in self.books:
            print(key)
    def print_users(self):
        for user in self.users:
            print(user)
    def most_read_book(self):
        mostread = None
        highestreadcount = 0
        for book in self.books:
            value = self.books.get(book)
            if value > highestreadcount:
                mostread = book
                highestreadcount = value
        print("The most read book is {} with {} reads!".format(mostread, highestreadcount))
        return mostread
    def highest_rated_book(self):
        highestrated = None
        rating = 0
        for book in self.books:
            if book.get_average_rating() > rating:
                highestrated = book
                rating = book.get_average_rating()
        print("The highest rated book is {} with a rating of {}.".format(highestrated,rating))
        return highestrated
    def most_positive_user(self):
        mostpositive = None
        highestaverage = 0
        for user in self.users:
            userobj = self.users.get(user)
            if userobj.get_average_rating() > highestaverage:
                mostpostive = userobj
                highestaverage = userobj.get_average_rating()
        print("The most positive user is {}, with an average rating of {}".format(mostpostive.name, highestaverage))
        return mostpostive
