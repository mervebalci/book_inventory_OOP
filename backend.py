import sqlite3


class Database:

    # Creating __init__ Method (not function anymore) which means initialize an object.
    # In other programming languages this is called as constructor (in JAVA). So, it constructs the objects.
    # We need to add self. prefix in front of each variable (connection, cursor) and they will be called attributes.
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connection.commit()

    # When this __init__ code is executed, we create a connection there and we keep the connection open.
    # So, we need to remove the connection.close() code for each method (insert, view, search, delete, update)
    # Now, we have a connection open there, we don't need to establish a new one in each method.
    # We also don't need to create a cursor object in each method, because the cursor object is being created already in __init__ method.
    # So, we removed "connection=sqlite3.connect()" and "cursor=conncetion.cursor()" from each method except __init__


    # Creating an Insert Method (not function anymore) to ADD some data in database
    def insert(self, title, author, year, isbn):
        # connection = sqlite3.connect(db)
        # cursor = connection.cursor()
        self.cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.connection.commit()
        # connection.close()


    # Creating a View Method (not function anymore) to fetch all the rows of the table
    def view(self):
        # connection = sqlite3.connect(db)
        # cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        # connection.close()
        return rows


    # Creating a Search Method (not function anymore)
    def search(self, title = "", author = "", year = "", isbn = ""):
        # connection = sqlite3.connect(db)
        # cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        # connection.close()
        return rows


    # Creating a Delete Method (not function anymore)
    def delete(self, id):
        # connection = sqlite3.connect(db)
        # cursor = connection.cursor()
        self.cursor.execute("DELETE FROM book WHERE id =?", (id,))
        self.connection.commit()
        # connection.close()


    # Creating an Update Method (not function anymore)
    def update(self, id, title, author, year, isbn):
        # connection = sqlite3.connect(db)
        # cursor = connection.cursor()
        self.cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.connection.commit()
        # connection.close()
    
    
    # First time when we click on View All button, this method was executed.
    # So the cursor object was able to fetch the data. And then we closed the connection. 
    # When we click on the button second time, view method faced a close connection. And we got a ProgrammingError.
    # ProgrammingError: Cannot operate on a closed database.
    # As a result, we removed connection.close() function from each method


    # At the end, better to add a close() method or we may get some problems later with some methods that have not been committed.
    # CLOSING THE CLASS
    def __del__(self):
        self.connection.close()


    # insert("The Ocean", "Neil Dawson", 1981, 822547838)
    # insert("Secret Garden", "Rosalia Demore", 1992, 864899713)
    # insert("Cosmic Universe", "Mark Albert Simpson", 2002, 924687819)

    # delete(2)

    # update(4, "Cosmos", "Mark Albert Tyson", 2003, 924811915)

    # print(view())

    # print(search(author = "Rosalia Demore"))