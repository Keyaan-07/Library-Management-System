import mysql.connector
from datetime import datetime

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
		updateUser() 
	elif userChoice == 3:
		exiting()
	else:
		validOption()

def notBook(bookId):
	print(f'The book of book id "{bookId}" does not available in the digital library.')
	print("--------------------------")
	updateBookMenu()

# Function to update book details
def updateBook():
    print("--------------------------")
    print("Update Book Details")
    print("--------------------------")
    print("1. Update the Book ID")
    print("2. Update the Book Name")
    print("3. Update the Book Publication Year")
    print("4. Update the Book Author Name")
    print("5. Home")
    print("6. Back")
    print("7. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    c.execute("SELECT bookId FROM books")
    result = c.fetchall()
    db.commit()

    if userChoice == 1:
        currentBookId = int(input("Enter the Current Book ID : "))
        newBookId = int(input("Enter the New Book ID : "))

        if (currentBookId,) in result:
            c.execute("UPDATE books SET bookId=%s WHERE bookId=%s", (newBookId, currentBookId))
            db.commit()

            print("Book ID changed Successfully!")
            print("--------------------------")
            updateBookMenu()
        else:
            notBook(currentBookId)

    elif userChoice == 2:
        bookId = int(input("Enter the Book ID : "))
        newBookName = input("Enter the New Book Name : ")

        if (bookId,) in result:
            c.execute("UPDATE books SET bookName=%s WHERE bookId=%s", (newBookName, bookId))
            db.commit()

            print("Book Name changed Successfully!")
            print("--------------------------")
            updateBookMenu()
        else:
            notBook(bookId)

    elif userChoice == 3:
        bookId = int(input("Enter the Current Book ID : "))
        newPublicationYear = input("Enter the New Publication Year : ")

        if (bookId,) in result:
            c.execute("UPDATE books SET publicationYear=%s WHERE bookId=%s", (newPublicationYear, bookId))
            db.commit()

            print("Book Publication Year changed Successfully!")
            print("--------------------------")
            updateBookMenu()
        else:
            notBook(bookId)

    elif userChoice == 4:
        bookId = int(input("Enter the Current Book ID : "))
        newAuthor = input("Enter the New Author Name : ")

        if (bookId,) in result:
            c.execute("UPDATE books SET author=%s WHERE bookId=%s", (newAuthor, bookId))
            db.commit()

            print("Book Author Name changed Successfully!")
            print("--------------------------")
            updateBookMenu()
        else:
            notBook(bookId)

    elif userChoice == 5:
        home() # upcoming function
    elif userChoice == 6:
        modifyBook() # upcoming function
    elif userChoice == 7:
        exiting()
    else:
        validOption()

# Function to display the issue book menu and handle user choices
def issueBookMenu():
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

# Function to issue a book
def issueBook():
    print("--------------------------")
    print("Issue Book")
    print("--------------------------")
    bookId = int(input("Enter the Book ID to be Issued: "))
    userId = int(input("Enter the User ID to whom Book will be Issued: "))

    c.execute("SELECT userId FROM users")
    result1 = c.fetchall()
    c.execute("SELECT bookId FROM books")
    result2 = c.fetchall()
    c.execute("SELECT issueStatus FROM books WHERE bookId=%s", (bookId,))
    result3 = c.fetchall()
    db.commit()

    if (userId,) in result1:
        if (bookId,) in result2:
            if result3[0][0] == "not issued":
                c.execute("UPDATE books SET issueDate = CURRENT_DATE WHERE bookId = %s", (bookId,))
                c.execute("UPDATE books SET issueTime = CURRENT_TIME WHERE bookId = %s", (bookId,))
                c.execute("UPDATE books SET issueStatus = 'issued' WHERE bookId = %s", (bookId,))
                c.execute("UPDATE books SET issuedUserId = %s WHERE bookId = %s", (userId, bookId))
                db.commit()
                c.execute("select issuedUserId,bookName,issueDate,issueTime from books where bookId=%s",(bookId,),)
                result = c.fetchall()
                c.execute("INSERT INTO issuedBooksDetails (userId,bookId,bookName,issueDate,issueTime) VALUES (%s, %s, %s, %s, %s)",(result[0][0], bookId, result[0][1], result[0][2],result[0][3]),)
                db.commit()

                print(f'Book of Book Id "{bookId}" is issued successfully to the User of User Id "{userId}".')
                print("--------------------------")
                returnPolicy()
                issueBookMenu()
            else:
                print(f'The book of book id "{bookId}" is already issued by another user.')
                print("--------------------------")
                issueBookMenu()
        else:
            print(f"Book with book id {bookId} does not exist in the digital library.")
            print("--------------------------")
            issueBookMenu()
    else:
        print(f"User with user id {userId} does not exist in the digital library.")
        print("--------------------------")
        issueBookMenu()

# Function to display the return book menu and handle user choices
def returnBookMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home() # upcoming function
    elif userChoice == 2:
        admin() # upcoming function
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to return a book
def returnBook():
    print("--------------------------")
    print("Return Book")
    print("--------------------------")
    bookId = int(input("Enter the Book ID to be Returned: "))

    c.execute("SELECT bookId FROM books")
    result1 = c.fetchall()
    c.execute("SELECT issueStatus FROM books WHERE bookId=%s", (bookId,))
    result2 = c.fetchall()
    db.commit()

    if (bookId,) in result1:
        if result2[0][0] == "issued":
            c.execute("UPDATE books SET returnDate = CURRENT_DATE WHERE bookId = %s", (bookId,))
            c.execute("UPDATE books SET returnTime = CURRENT_TIME WHERE bookId = %s", (bookId,))
            c.execute("UPDATE books SET issueStatus = 'not issued' WHERE bookId = %s", (bookId,))
            db.commit()

            c.execute("SELECT issuedUserId, returnDate, returnTime FROM books WHERE bookId=%s", (bookId,))
            result = c.fetchall()
            c.execute("UPDATE issuedBooksDetails SET returnDate = %s, returnTime = %s WHERE userId = %s AND bookId = %s",
                      (result[0][1], result[0][2], result[0][0], bookId))
            db.commit()

            c.execute("UPDATE books SET issuedUserId = NULL WHERE bookId = %s", (bookId,))
            db.commit()

            print(f'The book of book id "{bookId}" is returned successfully.')

            c.execute("SELECT issueDate FROM books WHERE bookId = %s", (bookId,))
            issueDate = c.fetchall()
            c.execute("SELECT returnDate FROM books WHERE bookId = %s", (bookId,))
            returnDate = c.fetchall()
            db.commit()

            d1 = datetime.strptime(f"{issueDate[0][0]}", "%Y-%m-%d")
            d2 = datetime.strptime(f"{returnDate[0][0]}", "%Y-%m-%d")
            dateDifference = d2 - d1

            if dateDifference.days > 14:
                extraDays = dateDifference.days - 14
                fine = extraDays * 5
                print("Fine(in Rs.) : ", fine)
                c.execute("UPDATE issuedBooksDetails SET fineInRs=%s WHERE userId=%s AND bookId=%s",
                          (fine, result[0][0], bookId))
                db.commit()
            else:
                fine = 0
                print("Fine(in Rs.) : ", fine)
                c.execute("UPDATE issuedBooksDetails SET fineInRs=%s WHERE userId=%s AND bookId=%s",
                          (fine, result[0][0], bookId))
                db.commit()

            print("--------------------------")
            returnBookMenu()
        else:
            print(f'The book of book id "{bookId}" is not issued by any user.')
            print("--------------------------")
            returnBookMenu()
    else:
        print(f"Book with book id {bookId} does not exist in the digital library.")
        print("--------------------------")
        returnBookMenu()

# Function to display the add user menu and handle user choices
def addUserMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home() # upcoming function
    elif userChoice == 2:
        modifyUser() # upcoming function
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to add a new user
def addUser():
    print("--------------------------")
    print("Add User")
    print("--------------------------")
    userId = int(input("Enter the User ID : "))
    userName = input("Enter the User Name : ")
    userPhoneNumber = input("Enter the User Phone Number : ")
    userEmailId = input("Enter the User Email ID : ")
    password = input("Enter the User Password : ")
    print("--------------------------")

    c.execute("SELECT userId FROM users")
    result = c.fetchall()
    db.commit()

    if (userId,) in result:
        print(f'The user with user number "{userId}" is already enrolled in the digital library.')
        print("--------------------------")
        addUserMenu()
    else:
        c.execute("INSERT INTO users (userId, userName, phoneNumber, emailId, password) VALUES (%s, %s, %s, %s, %s)",
                  (userId, userName, userPhoneNumber, userEmailId, password))
        db.commit()

        print("--------------------------")
        print("User added successfully!")
        print("--------------------------")
        addUserMenu()

# Function to display the delete user menu and handle user choices
def deleteUserMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home() # upcoming function
    elif userChoice == 2:
        modifyUser() # upcoming function
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to delete a user
def deleteUser():
    print("--------------------------")
    print("Delete User")
    print("--------------------------")
    userId = int(input("Enter the User ID : "))
    choice = input("Are you sure to delete the User? (Yes/No) : ")
    print("--------------------------")

    c.execute("SELECT userId FROM users")
    result = c.fetchall()
    db.commit()

    if choice.lower() in ["yes", "y"]:
        if (userId,) in result:
            c.execute("DELETE FROM users WHERE userId=%s", (userId,))
            db.commit()

            print("User deleted successfully!")
            print("--------------------------")
            deleteUserMenu()
        else:
            print(f'The user with user id "{userId}" is not enrolled in the digital library.')
            print("--------------------------")
            deleteUserMenu()
    elif choice.lower() in ["no", "n"]:
        print("--------------------------")
        print("User Not Deleted!")
        print("--------------------------")
        deleteUserMenu()
    else:
        validOption()

# Function to display the update user menu and handle user choices
def updateUserMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home() # upcoming function
    elif userChoice == 2:
        updateUser()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Helper function to display if a user does not exist
def notUser(userId):
    print(f'The user with user id "{userId}" is not enrolled in the digital library.')
    print("--------------------------")
    updateUserMenu()

# Function to update user details
def updateUser():
    print("--------------------------")
    print("Update User Details")
    print("--------------------------")
    print("1. Update the User ID")
    print("2. Update the User Name")
    print("3. Update the User Phone Number")
    print("4. Update the User Email ID")
    print("5. Update the User Password")
    print("6. Home")
    print("7. Back")
    print("8. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    c.execute("SELECT userId FROM users")
    result = c.fetchall()
    db.commit()

    if userChoice == 1:
        currentUserId = int(input("Enter the Current User ID : "))
        newUserId = int(input("Enter the New User ID : "))

        if (currentUserId,) in result:
            c.execute("UPDATE users SET userId=%s WHERE userId=%s", (newUserId, currentUserId))
            db.commit()

            print("User ID changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(currentUserId)

    elif userChoice == 2:
        userId = int(input("Enter the User ID : "))
        newUserName = input("Enter the New User Name : ")

        if (userId,) in result:
            c.execute("UPDATE users SET userName=%s WHERE userId=%s", (newUserName, userId))
            db.commit()

            print("User Name changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)

    elif userChoice == 3:
        userId = int(input("Enter the Current User ID : "))
        newPhoneNumber = input("Enter the New Phone Number : ")

        if (userId,) in result:
            c.execute("UPDATE users SET phoneNumber=%s WHERE userId=%s", (newPhoneNumber, userId))
            db.commit()

            print("User Phone Number changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)

    elif userChoice == 4:
        userId = int(input("Enter the Current User ID : "))
        newEmailId = input("Enter the New Email ID : ")

        if (userId,) in result:
            c.execute("UPDATE users SET emailId=%s WHERE userId=%s", (newEmailId, userId))
            db.commit()

            print("User Email ID changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)

    elif userChoice == 5:
        userId = int(input("Enter the Current User ID : "))
        newPassword = input("Enter the New Password : ")

        if (userId,) in result:
            c.execute("UPDATE users SET password=%s WHERE userId=%s", (newPassword, userId))
            db.commit()

            print("User Password changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)

    elif userChoice == 6:
        home() # upcoming function
    elif userChoice == 7:
        modifyUser() # upcoming function
    elif userChoice == 8:
        exiting()
    else:
        validOption()
