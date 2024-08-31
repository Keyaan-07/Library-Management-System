import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library",
)
c = db.cursor()

# Function to display the return policy information
def returnPolicy():
    print("Return Policy : ")
    print("The issued book should be returned within 14 days(2 weeks).")
    print("If the user kept the issued book for more than 14 days, then the user have to pay ₹5 as fine for each extra day the user kept the issued book.")
    print("--------------------------")

# Function to display a message for an invalid option
def validOption():
    print("Please enter a valid option!")
    print("--------------------------")

# Function to handle program exit
def exiting():
    print("\033[3;34m--------------------------\033[0;0m")
    print("\033[3;33mExiting the program.")
    print("Thank You!\033[0;0m")
    print("\033[3;34m--------------------------\033[0;0m")
    exit()

# Function to calculate the length of a given integer after converting it to a string
def length(i):
    s = str(i)
    length = len(s) + 2
    return length

# Function to display the user menu and handle user choices
def userMenu():
    print("1. Add Note")
    print("2. Home")
    print("3. Back")
    print("4. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        addNote() # upcoming function
    elif userChoice == 2:
        home() # upcoming function
    elif userChoice == 3:
        user() # upcoming function
    elif userChoice == 4:
        exiting()
    else:
        validOption()

# Function to display information about the library
def aboutLibrary():
    c.execute("SELECT userName FROM users WHERE adminStatus='admin'")
    userName = c.fetchall()

    c.execute("SELECT * FROM books")
    totalBooks = c.fetchall()

    c.execute("SELECT * FROM users")
    totalUsers = c.fetchall()
    db.commit()

    print("--------------------------")
    print("About Library")
    print("--------------------------")
    print("Year of Library's Establishment : ", 2024)
    print("Name of the Librarian : ", userName[0][0])
    print("Total Number of Books Available in the Library : ", len(totalBooks))
    print("Total Number of Users Enrolled in the Library : ", len(totalUsers))
    print("--------------------------")
    userMenu()

# Function to display the list of books in the library
def displayBooks():
    print("--------------------------")
    print("Display Books")
    print("--------------------------")
    c.execute("SELECT * FROM books ORDER BY bookId")
    result = c.fetchall()
    db.commit()

    if result:
        print("Books available in the Digital Library are :")
        print("--------------------------")
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. Book ID : {row[0]}")
            print(" " * r + f"Book Name : {row[1]}")
            print(" " * r + f"Publication Year : {row[2]}")
            print(" " * r + f"Author Name : {row[7]}")
            print(" " * r + f"Issue Status : {row[8]}")
            print("--------------------------")
        userMenu()
    else:
        print("No books found.")
        print("--------------------------")
        userMenu()

# Search books menu options
def searchBooksMenu():
    print("1. Add Note")
    print("2. Home")
    print("3. Back")
    print("4. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))

    if userChoice == 1:
        addNote() # upcoming function
    elif userChoice == 2:
        home() # upcoming function
    elif userChoice == 3:
        searchBooks()
    elif userChoice == 4:
        exiting()
    else:
        validOption()

# Function to search books by Book ID
def searchBooksbyId():
    print("--------------------------")
    print("Search Books by Book ID")
    print("--------------------------")
    bookId = int(input("Enter the Book ID to search the Book : "))
    print("--------------------------")

    c.execute("SELECT * FROM books WHERE bookId=%s", (bookId,))
    result = c.fetchall()
    db.commit()

    if result:
        print(f'Book available in the Digital Library with the Book ID "{bookId}" is :')
        print("--------------------------")
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. Book ID : {row[0]}")
            print(" " * r + f"Book Name : {row[1]}")
            print(" " * r + f"Publication Year : {row[2]}")
            print(" " * r + f"Author Name : {row[7]}")
            print(" " * r + f"Issue Status : {row[8]}")
            print("--------------------------")
        searchBooksMenu()
    else:
        print(f'No book found with the book id "{bookId}".')
        print("--------------------------")
        searchBooksMenu()

# Function to search books by keyword
def searchBooksbyKeyword():
    print("--------------------------")
    print("Search Books by Keyword")
    print("--------------------------")
    keyword = input("Enter a Keyword to search Books : ")
    print("--------------------------")

    c.execute("SELECT * FROM books WHERE bookName LIKE '%{}%' ORDER BY bookId".format(keyword))
    result = c.fetchall()
    db.commit()

    if result:
        print(f'Books available in the Digital Library with the Keyword "{keyword}" are :')
        print("--------------------------")
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. Book ID : {row[0]}")
            print(" " * r + f"Book Name : {row[1]}")
            print(" " * r + f"Publication Year : {row[2]}")
            print(" " * r + f"Author Name : {row[7]}")
            print(" " * r + f"Issue Status : {row[8]}")
            print("--------------------------")
        searchBooksMenu()
    else:
        print(f'No books found with the keyword "{keyword}".')
        print("--------------------------")
        searchBooksMenu()

# Function to display search options for books
def searchBooks():
    print("--------------------------")
    print("Search Books")
    print("--------------------------")
    print("1. Search by Book ID")
    print("2. Search by Keyword")
    print("3. Home")
    print("4. Back")
    print("5. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        searchBooksbyId()
    elif userChoice == 2:
        searchBooksbyKeyword()
    elif userChoice == 3:
        home() # upcoming function
    elif userChoice == 4:
        user() # upcoming function
    elif userChoice == 5:
        exiting()
    else:
        validOption()

# Function to display the add book menu and handle user choices
def addBookMenu():
	# Add book menu options
	print("1. Home")
	print("2. Back")
	print("3. Exit")
	userChoice = int(input("Enter your Choice to Continue : "))
	print("--------------------------")
    # User choices handling
	if userChoice == 1:
		home() # upcoming function
	elif userChoice == 2:
		modifyBook() # upcoming function
	elif userChoice == 3:
		exiting()
	else:
		validOption()

# Function to add a new book to the library
def addBook():
    print("--------------------------")
    print("Add Book")
    print("--------------------------")
    bookId = int(input("Enter the Book ID : "))
    bookName = input("Enter the Book Name : ")
    publicationYear = int(input("Enter the Book Publication Year : "))
    author = input("Enter the Book Author Name : ")
    print("--------------------------")

    c.execute("SELECT bookId FROM books")
    result = c.fetchall()
    db.commit()

    if (bookId,) in result:
        print(f'The book of book id "{bookId}" is already available in the digital library.')
        print("--------------------------")
        addBookMenu()
    else:
        c.execute(
            "INSERT INTO books (bookId, bookName, publicationYear, author) VALUES (%s, %s, %s, %s)",
            (bookId, bookName, publicationYear, author),
        )
        db.commit()

        print("Book added Successfully!")
        print("--------------------------")
        addBookMenu()

def deleteBookMenu():
	# Delete book menu options
	print("1. Home")
	print("2. Back")
	print("3. Exit")
	userChoice = int(input("Enter your Choice to Continue : "))
	print("--------------------------")

	# User choices handling
	if userChoice == 1:
		home() # upcoming function
	elif userChoice == 2:
		admin() # upcoming function
	elif userChoice == 3:
		exiting()
	else:
		validOption()

# Function to delete a book from the library
def deleteBook():
    print("--------------------------")
    print("Delete Book")
    print("--------------------------")
    bookId = int(input("Enter the Book ID : "))
    choice = input("Are you sure to delete the Book? (Yes/No) : ")
    print("--------------------------")

    c.execute("SELECT bookId FROM books")
    result = c.fetchall()
    db.commit()

    if choice.lower() in ["yes", "y"]:
        if (bookId,) in result:
            c.execute("DELETE FROM books WHERE bookId=%s", (bookId,))
            db.commit()

            print("Book deleted Successfully!")
            print("--------------------------")
            deleteBookMenu()
        else:
            print(f'The book of book id "{bookId}" does not exist in the digital library.')
            print("--------------------------")
            deleteBookMenu()
    elif choice.lower() in ["no", "n"]:
        print("--------------------------")
        print("Book Not Deleted!")
        print("--------------------------")
        deleteBookMenu()
    else:
        validOption()

# Update book menu options
def updateBookMenu():
	print("1. Home")
	print("2. Back")
	print("3. Exit")
	userChoice = int(input("Enter your Choice to Continue : "))
	print("--------------------------")

	# User choices handling
	if userChoice == 1:
		home() # upcoming function
	elif userChoice == 2:
		updateUser() # upcoming function
	elif userChoice == 3:
		exiting()
	else:
		validOption()

def notBook(bookId):
	print(f'The book of book id "{bookId}" does not available in the digital library.')
	print("--------------------------")
	updateBookMenu()
