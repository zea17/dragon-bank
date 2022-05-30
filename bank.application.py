from datetime import datetime
import random
import json


def get_data():
    """
    Reads the bank information from the data file.
    """
    f = open("bank.json", "r")
    data = f.read()
    return json.loads(data)


def set_data(data):
    """
    Writes the bank information into the data file
    """
    f = open("bank.json", "w")
    f.write(json.dumps(data))


def generate_account_number():
    """
    Generates a new unique account number
    """
    prefix = "17172424"
    result = ""
    for _ in range(0, 8):
        random_number = random.randint(1, 9)
        result += str(random_number)

    return prefix + result


def perform_transaction(sender_number, receiver_number, amount):
    """
    Given two account numbers and a transaction amount, this will move
    the money from the sender account to the recepient account.
    """
    users = get_data()

    if sender_number in users:
        print("Did not found the account with number: " + sender_number)
        return

    if receiver_number in users:
        print("Did not found the account with number: " + receiver_number)
        return

    if sender_number in users and receiver_number in users:
        if users[sender_number]["balance"] >= amount:
            users[sender_number]["balance"] -= amount
            users[receiver_number]["balance"] += amount

    set_data(users)


def create_new_user(full_name, balance, gender):
    """
    Creatas a new user with the given information
    """
    users = get_data()
    date = datetime.today().strftime('%Y-%m-%d')
    users[generate_account_number()] = {
        "full_name": full_name,
        "gender": gender,
        "balance": balance,
        "account_creation_date": date
    }
    set_data(users)


def display_menu():
    """
    Displays the welcome menu and asks the user for a
    command to perform (which then performs)
    """
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

    user_choice = int(input("☞ enter your choice:"))
    if user_choice == 1:
        user_name = input("Full Name: ")
        balance = float(input("Balance: "))
        gender = input("Gender: ")
        create_new_user(user_name, balance, gender)
    if user_choice == 2:
        sender = input("Sender's Account Number: ")
        receiver = input("Recipient's Account Number: ")
        amount = float(input("Transaction Amount: "))
        perform_transaction(sender, receiver, amount)


display_menu()
