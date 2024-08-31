import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library",
)
c = db.cursor()

def returnPolicy():
    print("Return Policy : ")
    print("The issued book should be returned within 14 days(2 weeks).")
    print("If the user kept the issued book for more than 14 days, then the user have to pay ₹5 as fine for each extra day the user kept the issued book.")
    print("--------------------------")
  
def validOption():
    print("Please enter a valid option!")
    print("--------------------------")
  
def exiting():
    print("\033[3;34m--------------------------\033[0;0m")
    print("\033[3;33mExiting the program.")
    print("Thank You!\033[0;0m")
    print("\033[3;34m--------------------------\033[0;0m")
    exit()
