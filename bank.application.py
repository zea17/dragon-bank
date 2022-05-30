from datetime import datetime
import random
import json

def get_data ():
    f = open("bank.json","r")
    data = f.read()
    return json.loads(data)


def set_data (data):
    f = open("bank.json","w")
    f.write(json.dumps(data))

    

def AccountNumber():
    prefix = "17172424"
    result = ""
    for i in range (0,8):
        random_number = random.randint(1, 9)
        result += str(random_number)
    
    return prefix + result


def transaction(sender,receiver,amount):
    users = get_data()
    if sender in users and receiver in users:
        if users[sender]["balance"] >= amount:
            users[sender]["balance"] -= amount
            users[receiver]["balance"] += amount
    set_data(users)


def create_new_user(user_name,balance,gender):
    users = get_data()
    date = datetime.today().strftime('%Y-%m-%d')
    users[user_name] = {
        "gender": gender,
        "account_number": AccountNumber(),
        "balance": balance,
        "account_creation_date": date
    }
    set_data(users)

def display_menu():
    print("             ＄ WELCOME ＄")
    print("▽▲▽▲▽▲▽ you are in dragon bank ▽▲▽▲▽▲▽")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►1∙Create new account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►2∙Make Transaction")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►3∙update information of existing account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►4∙removing existing account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►5∙check the details of existing account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►6∙view customer's list")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►7∙exit")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")

    user_choice = int(input("enter your choice:"))
    if user_choice == 1:
       user_name = input("name: ")
       balance = float(input("balance: "))
       gender = input("gender: ")
       create_new_user(user_name,balance,gender)
    if user_choice == 2:
        sender = input("Sender's name?")
        receiver = input("Recipient's name")
        amount = float(input("amount"))
        transaction(sender,receiver,amount)

display_menu()    


    