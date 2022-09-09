from ast import Return
import time
from MianPage import mainPage

def entryInputValidation():
    x = input("Enter Your Choice: ")
    if ((x.isdigit() == True) and int(x) in [1, 2]):
        return int(x)
    else :
        print ("Invalid Input")
        return entryInputValidation()


#User Names#####################
def enterFName():
    x = input("Enter your First Name: ")
    if (x.isalpha() == True):
        return x
    else:
        print("Invalid Input")
        return enterFName()


def enterSName():
    x = input("Enter your second Name: ")
    if (x.isalpha() == True):
        return x
    else:
        print("Invalid Input")
        return enterSName()


#Email############################
import re


def enteremail():
    x = input("Enter email: ")
    if (emailvalidator(x) == True):
        return x
    else:
        print("Invalid Input")
        return enteremail()


def emailvalidator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


#Password####################################33

def enterPassword():
    password1=input("enter your password")
    password2=input("confirm your password")
    if (re.fullmatch(password1,password2)):
        return password1
    else :
        print("Password are not matched")
        return enterPassword()

#Phone############################33

def enterPhone():
    x = input("Enter Your Phone: ")
    if (re.match(r"^01[0-2,5]\d{1,8}$", x)):
        return x
    else:
        print("Invalid Input")
        return enterPhone()


#  Saved Data ###############################

def saveData(data):
    file = open('usersdata.txt', 'a')
    file.writelines(data)
    file.close


def Registration():
    FirstName = enterFName()
    secondName = enterSName()
    email = enteremail()
    Password = enterPassword()
    phone = enterPhone()
    id = round(time.time())
    data = f"{id}:{email}:{Password}:{FirstName}:{secondName}:{phone}'\n'"
    saveData(data)

def checkExistans(email,password):
    file = open("usersdata.txt", "r")
    data = file.readlines()
    for i in data:
        d = i.split(":")
        if (d[1] == email and d[2] == password):
            return d[0]
        else:
            return Login()

def Login():
    print("---------LOGIN------------")
    email=input("EMAIL : ")
    password=input("Password: ")
    user_id=checkExistans(email,password)
    mainPage(user_id)


def entryPage():
    print("""============ Crowd-Funding Entry Page =========== 
    1) Registration
    2) Login """)
    choice = entryInputValidation()
    if (choice == 1):
        Registration()
    elif (choice == 2):
        Login()
