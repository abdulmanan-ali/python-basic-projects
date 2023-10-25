class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def DisplayAvailableBooks(self):
        print("Books Present in this library are ")
        # for book in self.books:
        #     print(" *" + book)
        for index, book in enumerate(self.books):
            print(f" \t{index + 1}: {book}")

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued this book {bookName}. please keep it safe and return in 30 days ")
            self.books.remove(bookName)
            return True
        else:
            print(
                f"Book Name {bookName} isn't available. This book is has already been issued to someone else ")
            return False

    def returnBooks(self, bookName):
        self.books.append(bookName)
        print(
            f"Thanks you to returning the {bookName} book hope you read and enjoying it ")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input(
            "Enter the Name of the book that you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(
        ["Python", "Algorithms", "Flask", "Django", "C++"])
    # centralLibrary.DisplayAvailableBooks()
    student = Student()

    while (True):
        welcomeLibrary = '''=====Welcome Our Library=====
        Pleae Choose an option:
        1. List of all Books
        2. Borrow Books
        3. Return Books
        4. Exit the Library
        '''
        print(welcomeLibrary)
        chooseOption = int(input("Choose your above option "))
        if chooseOption == 1:
            centralLibrary.DisplayAvailableBooks()
        elif chooseOption == 2:
            # student = Student()
            # bookName = student.requestBook()
            centralLibrary.borrowBooks(student.requestBook())
        elif chooseOption == 3:
            # student = Student()
            # bookName = student.returnBook()
            centralLibrary.returnBooks(student.returnBook())
        elif chooseOption == 4:
            print("Thanks for joining our Library ")
            exit()
        else:
            print("Invalid Choice :( \n")
