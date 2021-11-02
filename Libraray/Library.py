import datetime


def date_time():
    return datetime.datetime.now()


class liabrary:
    liabrary_name = "Al- Hashar -kitaab-khana"
    liabrary_Since = '1972'
    In_stock_books = {'1': "In Search of Lost Time by Marcel Proust", '2': 'Ulysses by James Joyce',
                      '3': 'Don Quixote by Miguel de Cervantes',
                      '4': 'One Hundred Years of Solitude by Gabriel Garcia Marquez',
                      '5': 'The Great Gatsby by F', '6': 'Moby Dick by Herman Melville',
                      '7': 'Hamlet by William Shakespeare', '8': 'The Odyssey by Homer',
                      '9': 'Madame Bovary by Gustave Flaubert', '10': 'The Divine Comedy by Dante Alighieri'}
    reserved_books = {}

    file = open('Library.txt', 'a')

    def __init__(self, First_name, Last_name):
        self.first_name = First_name
        self.last_name = Last_name

    old_key = ''

    @classmethod
    def Display_Books(cls):
        print("""BOOKS COLLECTION """)

        for keys in sorted(liabrary.In_stock_books):
            print(keys + '    :    ' + cls.In_stock_books[keys])

    def select_book(self, Book_name):
        for keys in liabrary.In_stock_books:

            if liabrary.In_stock_books[keys] == Book_name:
                liabrary.old_key = keys
                new_key = f'is reserved by : {self.first_name} {self.last_name} '
                liabrary.reserved_books.update({new_key: Book_name})
                liabrary.In_stock_books.pop(keys)
                datetim = str(date_time())
                liabrary.file.write(
                    str(liabrary.reserved_books[
                            new_key]) + f' is reserved by {self.first_name} {self.last_name} at {datetim} ' + chr(10))

                break
        else:
            print("Book is not avaliable in our stock ")

    def return_book(self, Book_name):
        for keys in liabrary.reserved_books:
            if liabrary.reserved_books[keys] == Book_name:
                liabrary.In_stock_books.update({liabrary.old_key: Book_name})
                datetim = str(date_time())

                liabrary.file.write(
                    str(liabrary.In_stock_books[
                            self.old_key]) + f' is returned by {self.first_name} {self.last_name} at {datetim}' + chr(
                        10))
                liabrary.reserved_books.pop(keys)
                break


class student(liabrary):
    def __init__(self, First_Name, Last_name, Email):
        self.first_name = First_Name
        self.last_name = Last_name
        self.email = Email

    def request_book(self, book_name):
        return self.select_book(book_name)

    def return_book_back(self, book_name):
        return self.return_book(book_name)


if __name__ == '__main__':
    hashar = student('Hashar', 'Mujahid', 'hasharmujahid@gmail.com')
    student2 = student('Abdullah', 'Chudaray', 'Abdullahchudaray@gamil.com')
    hashar.request_book('Don Quixote by Miguel de Cervantes')
    liabrary.Display_Books()
    hashar.return_book_back('Don Quixote by Miguel de Cervantes')
    student2.request_book('Don Quixote by Miguel de Cervantes')

    student2.return_book_back('Don Quixote by Miguel de Cervantes')
    liabrary.Display_Books()
