import mysql.connector
import pyfiglet
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
        addNote()
    elif userChoice == 2:
        home()
    elif userChoice == 3:
        user()
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

# Function to display books search menu
def searchBooksMenu():
    print("1. Add Note")
    print("2. Home")
    print("3. Back")
    print("4. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        addNote()
    elif userChoice == 2:
        home()
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
        home()
    elif userChoice == 4:
        user()
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
		home()
	elif userChoice == 2:
		modifyBook()
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
		home()
	elif userChoice == 2:
		admin()
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
		home()
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
        home()
    elif userChoice == 6:
        modifyBook()
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
        home()
    elif userChoice == 2:
        admin()
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
        home()
    elif userChoice == 2:
        admin()
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
        home()
    elif userChoice == 2:
        modifyUser()
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
        home()
    elif userChoice == 2:
        modifyUser()
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
        home()
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
        home()
    elif userChoice == 7:
        modifyUser()
    elif userChoice == 8:
        exiting()
    else:
        validOption()

# Function to modify users (add, delete, update)
def modifyUser():
    print("--------------------------")
    print("Modify User")
    print("--------------------------")
    print("1. Add User")
    print("2. Delete User")
    print("3. Update User Details")
    print("4. Home")
    print("5. Back")
    print("6. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        addUser()
    elif userChoice == 2:
        deleteUser()
    elif userChoice == 3:
        updateUser()
    elif userChoice == 4:
        home()
    elif userChoice == 5:
        admin()
    elif userChoice == 6:
        exiting()
    else:
        validOption()

# Display users menu options
def displayUsersMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))

    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        admin()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to display the users enrolled in the library
def displayUsers():
    print("--------------------------")
    print("Display Users")
    print("--------------------------")
    c.execute("SELECT * FROM users ORDER BY userId")
    result = c.fetchall()
    db.commit()

    if result:
        print("Users enrolled in the Digital Library are :")
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. User ID : {row[0]}")
            print(" " * r + f"User Name : {row[1]}")
            print(" " * r + f"Phone Number : {row[2]}")
            print(" " * r + f"Email ID : {row[3]}")
            print(" " * r + f"Admin Status : {row[5]}")
            print("--------------------------")
        displayUsersMenu()
    else:
        print("No users found.")
        print("--------------------------")
        displayUsersMenu()

# Function to display user search options
def searchUsersMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))

    if userChoice == 1:
        home()
    elif userChoice == 2:
        searchUsers()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to search users by User ID
def searchUsersbyId():
    print("--------------------------")
    print("Search Users by User ID")
    print("--------------------------")
    userId = int(input("Enter the User ID to search the User : "))

    c.execute("SELECT * FROM users WHERE userId=%s", (userId,))
    result = c.fetchall()
    db.commit()

    if result:
        print(f'User enrolled in the Digital Library with the User ID "{userId}" is :')
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. User ID : {row[0]}")
            print(" " * r + f"User Name : {row[1]}")
            print(" " * r + f"Phone Number : {row[2]}")
            print(" " * r + f"Email ID : {row[3]}")
            print(" " * r + f"Admin Status : {row[5]}")
            print("--------------------------")
        searchUsersMenu()
    else:
        print(f'No user found with the user id "{userId}".')
        print("--------------------------")
        searchUsersMenu()

# Function to search users by keyword
def searchUsersbyKeyword():
    print("--------------------------")
    print("Search Users by Keyword")
    print("--------------------------")
    keyword = input("Enter a Keyword to search Users : ")

    c.execute("SELECT * FROM users WHERE userName LIKE '%{}%' ORDER BY userId".format(keyword))
    result = c.fetchall()
    db.commit()

    if result:
        print(f'Users enrolled in the Digital Library with the Keyword "{keyword}" are :')
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. User ID : {row[0]}")
            print(" " * r + f"User Name : {row[1]}")
            print(" " * r + f"Phone Number : {row[2]}")
            print(" " * r + f"Email ID : {row[3]}")
            print(" " * r + f"Admin Status : {row[5]}")
            print("--------------------------")
        searchUsersMenu()
    else:
        print(f'No users found with the keyword "{keyword}".')
        print("--------------------------")
        searchUsersMenu()

# Function to search users
def searchUsers():
    print("--------------------------")
    print("Search Users")
    print("--------------------------")
    print("1. Search by User ID")
    print("2. Search by Keyword")
    print("3. Home")
    print("4. Back")
    print("5. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        searchUsersbyId()
    elif userChoice == 2:
        searchUsersbyKeyword()
    elif userChoice == 3:
        home()
    elif userChoice == 4:
        admin()
    elif userChoice == 5:
        exiting()
    else:
        validOption()

# Function to modify books (add, delete, update)
def modifyBook():
    print("--------------------------")
    print("Modify Book")
    print("--------------------------")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Update Book Details")
    print("4. Home")
    print("5. Back")
    print("6. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        addBook()
    elif userChoice == 2:
        deleteBook()
    elif userChoice == 3:
        updateBook()
    elif userChoice == 4:
        home()
    elif userChoice == 5:
        admin()
    elif userChoice == 6:
        exiting()
    else:
        validOption()

# Function to manage notes
def notes():
    print("--------------------------")
    print("Notes")
    print("--------------------------")
    print("1. Modify Note")
    print("2. Display Notes")
    print("3. Search Notes")
    print("4. Home")
    print("5. Back")
    print("6. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        modifyNote()
    elif userChoice == 2:
        displayNotes()
    elif userChoice == 3:
        searchNotes()
    elif userChoice == 4:
        home()
    elif userChoice == 5:
        user()
    elif userChoice == 6:
        exiting()
    else:
        validOption()

# Function to display the add note menu and handle user choices
def addNoteMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home()
    elif userChoice == 2:
        modifyNote()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to add a note
def addNote():
    print("--------------------------")
    print("Add Note")
    print("--------------------------")
    noteNumber = int(input("Enter the Note Number : "))
    noteTitle = input("Enter the Note Title : ")
    noteDescription = input("Enter the Note Description : ")
    print("--------------------------")

    c.execute("SELECT noteNumber FROM notes WHERE userId=%s", (USERID,))
    result = c.fetchall()
    db.commit()

    if (noteNumber,) in result:
        print(f'The note of note number "{noteNumber}" already exists in the digital library.')
        print("--------------------------")
        addNoteMenu()
    else:
        c.execute(
            "INSERT INTO notes (userId, noteNumber, noteTitle, noteDescription, updateDate, updateTime) VALUES (%s, %s, %s, %s, CURRENT_DATE, CURRENT_TIME)",
            (USERID, noteNumber, noteTitle, noteDescription),
        )
        db.commit()

        print(f'The note of note number "{noteNumber}" is added successfully.')
        print("--------------------------")
        addNoteMenu()

# Function to display delete note menu and handle user choices
def deleteNoteMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home()
    elif userChoice == 2:
        modifyNote()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to delete a note
def deleteNote():
    print("--------------------------")
    print("Delete Note")
    print("--------------------------")
    noteNumber = int(input("Enter the Note Number to Delete the Note : "))
    choice = input("Are you sure to delete the Note? (Yes/No) : ")
    print("--------------------------")

    c.execute("SELECT noteNumber FROM notes WHERE userId=%s", (USERID,))
    result = c.fetchall()
    db.commit()

    if choice.lower() in ["yes", "y"]:
        if (noteNumber,) in result:
            c.execute("DELETE FROM notes WHERE userId=%s AND noteNumber=%s", (USERID, noteNumber))
            db.commit()

            print(f'The note of note number "{noteNumber}" is deleted successfully.')
            print("--------------------------")
            deleteNoteMenu()
        else:
            print(f'The note of note number "{noteNumber}" does not exist in the digital library.')
            print("--------------------------")
            deleteNoteMenu()
    elif choice.lower() in ["no", "n"]:
        print("--------------------------")
        print("Note Not Deleted!")
        print("--------------------------")
        deleteNoteMenu()
    else:
        validOption()

# Function to display update notes menu and handle user choices
def updateNotesMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home()
    elif userChoice == 2:
        updateNotes()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Helper function to indicate a missing note
def notNoteNumber(noteNumber):
    print(f'The note of note number "{noteNumber}" does not exist in the digital library.')
    print("--------------------------")
    updateNotesMenu()

# Function to update notes
def updateNotes():
    print("--------------------------")
    print("Update Notes")
    print("--------------------------")
    print("1. Update the Note Number")
    print("2. Update the Note Title")
    print("3. Update the Note Description")
    print("4. Home")
    print("5. Back")
    print("6. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    c.execute("SELECT noteNumber FROM notes WHERE userId=%s", (USERID,))
    result = c.fetchall()
    db.commit()

    if userChoice == 1:
        currentNoteNumber = int(input("Enter the Current Note Number : "))
        newNoteNumber = int(input("Enter the New Note Number : "))

        if (currentNoteNumber,) in result:
            c.execute(
                "UPDATE notes SET noteNumber=%s, updateDate=CURRENT_DATE, updateTime=CURRENT_TIME WHERE userId=%s AND noteNumber=%s",
                (newNoteNumber, USERID, currentNoteNumber),
            )
            db.commit()

            print("Note Number changed Successfully!")
            print("--------------------------")
            updateNotesMenu()
        else:
            notNoteNumber(currentNoteNumber)

    elif userChoice == 2:
        noteNumber = int(input("Enter the Note Number : "))
        newTitle = input("Enter the New Note Title : ")

        if (noteNumber,) in result:
            c.execute(
                "UPDATE notes SET noteTitle=%s, updateDate=CURRENT_DATE, updateTime=CURRENT_TIME WHERE userId=%s AND noteNumber=%s",
                (newTitle, USERID, noteNumber),
            )
            db.commit()

            print("Note Title changed Successfully!")
            print("--------------------------")
            updateNotesMenu()
        else:
            notNoteNumber(noteNumber)

    elif userChoice == 3:
        noteNumber = int(input("Enter the Note Number : "))
        newDescription = input("Enter the New Note Description : ")

        if (noteNumber,) in result:
            c.execute(
                "UPDATE notes SET noteDescription=%s, updateDate=CURRENT_DATE, updateTime=CURRENT_TIME WHERE userId=%s AND noteNumber=%s",
                (newDescription, USERID, noteNumber),
            )
            db.commit()

            print("Note Description changed Successfully!")
            print("--------------------------")
            updateNotesMenu()
        else:
            notNoteNumber(noteNumber)

    elif userChoice == 4:
        home()
    elif userChoice == 5:
        modifyNote()
    elif userChoice == 6:
        exiting()
    else:
        validOption()

# Function to modify notes
def modifyNote():
    print("--------------------------")
    print("Modify Note")
    print("--------------------------")
    print("1. Add Note")
    print("2. Delete Note")
    print("3. Update Note Details")
    print("4. Home")
    print("5. Back")
    print("6. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        addNote()
    elif userChoice == 2:
        deleteNote()
    elif userChoice == 3:
        updateNotes()
    elif userChoice == 4:
        home()
    elif userChoice == 5:
        notes()
    elif userChoice == 6:
        exiting()
    else:
        validOption()


# Function to display notes
def displayNotesMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home()
    elif userChoice == 2:
        notes()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

# Function to display all notes
def displayNotes():
    print("--------------------------")
    print("Display Notes")
    print("--------------------------")
    c.execute("SELECT * FROM notes WHERE userId=%s ORDER BY noteNumber", (USERID,))
    result = c.fetchall()
    db.commit()

    if result:
        print("Notes available in the Digital Library are :")
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. Note Number : {row[1]}")
            print(" " * r + f"Note Title : {row[2]}")
            print(" " * r + f"Note Description : {row[3]}")
            print("--------------------------")
        displayNotesMenu()
    else:
        print("No notes found.")
        print("--------------------------")
        displayNotesMenu()

# Function to display search notes menu
def searchNotesMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home()
    elif userChoice == 2:
        searchNotes()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to search notes by note number
def searchNotesbyNoteNumber():
    print("--------------------------")
    print("Search Notes by Note Number")
    print("--------------------------")
    noteNumber = int(input("Enter the Note Number to search the Note : "))

    c.execute("SELECT * FROM notes WHERE userId=%s AND noteNumber=%s", (USERID, noteNumber))
    result = c.fetchall()
    db.commit()

    if result:
        print(f'Note available in the Digital Library with the Note Number "{noteNumber}" is :')
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. Note Number : {row[1]}")
            print(" " * r + f"Note Title : {row[2]}")
            print(" " * r + f"Note Description : {row[3]}")
            print("--------------------------")
        searchNotesMenu()
    else:
        print(f'No note found with the note number "{noteNumber}".')
        print("--------------------------")
        searchNotesMenu()

# Function to search notes by keyword
def searchNotesbyKeyword():
    print("--------------------------")
    print("Search Notes by Keyword")
    print("--------------------------")
    keyword = input("Enter a Keyword to search Notes : ")

    c.execute("SELECT * FROM notes WHERE userId=%s AND noteTitle LIKE '%{}%' ORDER BY noteNumber".format(keyword), (USERID,))
    result = c.fetchall()
    db.commit()

    if result:
        print(f'Notes available in the Digital Library with the Keyword "{keyword}" are :')
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. Note Number : {row[1]}")
            print(" " * r + f"Note Title : {row[2]}")
            print(" " * r + f"Note Description : {row[3]}")
            print("--------------------------")
        searchNotesMenu()
    else:
        print(f'No notes found with the keyword "{keyword}".')
        print("--------------------------")
        searchNotesMenu()

# Function to search notes
def searchNotes():
    print("--------------------------")
    print("Search Notes")
    print("--------------------------")
    print("1. Search by Note Number")
    print("2. Search by Keyword")
    print("3. Home")
    print("4. Back")
    print("5. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        searchNotesbyNoteNumber()
    elif userChoice == 2:
        searchNotesbyKeyword()
    elif userChoice == 3:
        home()
    elif userChoice == 4:
        notes()
    elif userChoice == 5:
        exiting()
    else:
        validOption()

def changeAdminMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        home()
    elif userChoice == 2:
        admin()
    elif userChoice == 3:
        exiting()
    else:
        validOption()

def changeAdmin():
    print("--------------------------")
    print("Change Admin")
    print("--------------------------")
    newAdminId = int(input("Enter the New Admin's User ID : "))
    newAdminPassword = input("Enter the New Admin's Password : ")
    choice = input("Are you sure to change the Admin? (Yes/No) : ")
    print("--------------------------")

    c.execute("SELECT password FROM users WHERE userId=%s", (newAdminId,))
    result = c.fetchall()
    db.commit()

    if choice.lower() in ["yes", "y"]:
        if len(result) == 0:
            print("Please enter a valid user id!")
        else:
            if newAdminPassword == result[0][0]:
                c.execute("UPDATE users SET adminStatus='not admin' WHERE adminStatus ='admin'")
                c.execute("UPDATE users SET adminStatus='admin' WHERE userId=%s", (newAdminId,))
                db.commit()

                print("Admin Changed Successfully!")
                print("--------------------------")
                changeAdminMenu()
            else:
                print("Please enter a valid password!")
    elif choice.lower() in ["no", "n"]:
        print("Admin Not Changed!")
        print("--------------------------")
        changeAdminMenu()
    else:
        validOption()

def authAdmin():
    print("--------------------------")
    print("Admin Authentication")
    print("--------------------------")
    adminId = int(input("Enter the Admin's User ID : "))
    adminPassword = input("Enter the Admin's User Password : ")

    c.execute("SELECT password FROM users WHERE userId=%s", (adminId,))
    result = c.fetchall()
    db.commit()

    if len(result) == 0:
        print("--------------------------")
        print("Please enter a valid user id!")
        print("--------------------------")
    else:
        if adminPassword == result[0][0]:
            global USERID
            USERID = adminId
            print("\033[0;35m--------------------------\033[0;0m")
            print("\033[0;36mAdmin is verified successfully.\033[0;0m")
            print("\033[0;35m--------------------------\033[0;0m")
            admin()
        else:
            print("Please enter a valid password!")
            print("--------------------------")

def admin():
    print("--------------------------")
    print("Admin")
    print("--------------------------")
    print("1.  Login into User Panel")
    print("2.  Modify User")
    print("3.  Display Users")
    print("4.  Search Users")
    print("5.  Modify Book")
    print("6.  Issue Book")
    print("7.  Return Book")
    print("8.  Change Admin")
    print("9.  Home")
    print("10. Back")
    print("11. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        user()
    elif userChoice == 2:
        modifyUser()
    elif userChoice == 3:
        displayUsers()
    elif userChoice == 4:
        searchUsers()
    elif userChoice == 5:
        modifyBook()
    elif userChoice == 6:
        issueBook()
    elif userChoice == 7:
        returnBook()
    elif userChoice == 8:
        changeAdmin()
    elif userChoice == 9:
        home()
    elif userChoice == 10:
        authAdmin()
    elif userChoice == 11:
        exiting()
    else:
        validOption()


def authUser():
    print("--------------------------")
    print("User Authentication")
    print("--------------------------")
    userId = int(input("Enter the User ID : "))
    password = input("Enter the User Password : ")

    c.execute("SELECT password FROM users WHERE userId=%s", (userId,))
    result = c.fetchall()
    db.commit()

    if len(result) == 0:
        print("--------------------------")
        print("Please enter a valid user id!")
        print("--------------------------")
    else:
        if password == result[0][0]:
            global USERID
            USERID = userId
            print("\033[0;35m--------------------------\033[0;0m")
            print("\033[0;36mUser is verified successfully.\033[0;0m")
            print("\033[0;35m--------------------------\033[0;0m")
            user()
        else:
            print("Please Enter a Valid Password!")
            print("--------------------------")

def user():
    print("--------------------------")
    print("User")
    print("--------------------------")
    print("1.  Login into Admin Panel")
    print("2.  About the Library")
    print("3.  Display Books")
    print("4.  Search Books")
    print("5.  Issued Books Details")
    print("6.  Notes")
    print("7.  Home")
    print("8.  Back")
    print("9.  Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")

    if userChoice == 1:
        admin()
    elif userChoice == 2:
        aboutLibrary()
    elif userChoice == 3:
        displayBooks()
    elif userChoice == 4:
        searchBooks()
    elif userChoice == 5:
        issuedBooksDetails()
    elif userChoice == 6:
        notes()
    elif userChoice == 7:
        home()
    elif userChoice == 8:
        authUser()
    elif userChoice == 9:
        exiting()
    else:
        validOption()


def issuedBooksDetails():
    print("--------------------------")
    print("Issued Books Details")
    print("--------------------------")
    returnPolicy()

    c.execute("SELECT * FROM issuedBooksDetails WHERE userId=%s ORDER BY bookId", (USERID,))
    result = c.fetchall()
    db.commit()

    if result == []:
        print("No Books Issued!")
        print("--------------------------")
        userMenu()
    else:
        i = 0
        for row in result:
            i += 1
            r = length(i)
            print(f"{i}. Book ID : {row[1]}")
            print(" " * r + "Book Name : ", row[2])
            print(" " * r + "Issue Date : ", row[3])
            print(" " * r + "Issue Time : ", row[4])
            print(" " * r + "Return Date : ", row[5])
            print(" " * r + "Return Time : ", row[6])
            print(" " * r + "Fine(in Rs.) : ", row[7])
            print("--------------------------")
        userMenu()


def home():
    while True:
        print("==========================")
        print("\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;0m")
        print("\033[1;31m"+ pyfiglet.figlet_format("Welcome to the", font="banner3",width=1000))
        print(pyfiglet.figlet_format("Digital Library", font="banner3",width=1000)+ "\033[0;0m")
        print("\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;0m")
        print("==========================")
        print("--------------------------")
        print("Home")
        print("--------------------------")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        userChoice = int(input("Enter your Choice to Continue : "))
        print("--------------------------")
        # Handle user choices
        if userChoice == 1:
            authAdmin()
        elif userChoice == 2:
            authUser()
        elif userChoice == 3:
            exiting()
        else:
            validOption()


# Call the main menu function
home()
