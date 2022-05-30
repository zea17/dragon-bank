

# ─── IMPORTS ────────────────────────────────────────────────────────────────────


from datetime import datetime
import random
import json
from os.path import exists


# ─── CONSTANTS ──────────────────────────────────────────────────────────────────


FILE_PATH = "bank.json"


# ─── DATABASE ───────────────────────────────────────────────────────────────────


def get_data():
    """
    Reads the bank information from the data file.
    """
    if not exists(FILE_PATH):
        return {}
    f = open(FILE_PATH, "rw")
    data = f.read()
    return json.loads(data)


def set_data(data):
    """
    Writes the bank information into the data file
    """
    f = open(FILE_PATH, "w")
    f.write(json.dumps(data))


# ─── ACCONUT NUMBER ─────────────────────────────────────────────────────────────


def generate_account_number():
    """
    Generates a new unique account number. The bank
    prefix number is 1717 2424, the 8 other digits are
    then generated randomly
    """
    prefix = "17172424"
    result = ""
    for _ in range(0, 8):
        random_number = random.randint(1, 9)
        result += str(random_number)

    return prefix + result


# ─── TRANSACTION ────────────────────────────────────────────────────────────────


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

    print("Transfered ", amount, "$ from account",
          sender_number, "to", receiver_number)


# ─── CREATE A NEW USER ──────────────────────────────────────────────────────────


def create_new_user(full_name, balance, gender):
    """
    Creatas a new user with the given information
    """
    users = get_data()
    date = datetime.today().strftime('%Y-%m-%d')
    account_number = generate_account_number()
    users[account_number] = {
        "full_name": full_name,
        "gender": gender,
        "balance": balance,
        "account_creation_date": date
    }
    set_data(users)
    print("created user with account number: ", account_number)


# ─── DELETE AN ACCOUNT ──────────────────────────────────────────────────────────


def delete_account(account_number):
    """
    Deletes an account if exists, otherwise displays an error
    """
    users = get_data()
    if account_number not in users:
        print("Did not found the account with number: " + account_number)
        return
    del users[account_number]
    set_data(users)
    print("Account number", account_number, "removed.")


# ─── DISPLAY INFORMATION OF A GIVEN ACCOUNT NUMBER ──────────────────────────────


def display_account_information_by_given_account_number(account_number):
    """
    Diplays the information about a given account number
    """
    users = get_data()
    user = users[account_number]
    print("---------------------------")
    print("Full name: ", user["full_name"])
    print("Account number: ", account_number)
    print("Gender: ", user["gender"])
    print("Balance: ", user["balance"])
    print("date: ", user["account_creation_date"])


# ─── DISPLAY ALL OF THE CUSTOMERS ───────────────────────────────────────────────


def display_all_of_the_customers():
    """
    Lists all of the users and their information
    one after the other.
    """
    users = get_data()
    for account_number in users:
        display_account_information_by_given_account_number(account_number)


# ─── DISPLAY MENU ───────────────────────────────────────────────────────────────


def display_menu():
    """
    Displays the welcome menu and asks the user for a
    command to perform (which then performs).

    This also acts as the UI and recieves the information
    regarding of the respective functions.
    """
    print("              ＄ WELCOME ＄")
    print("  ▽▲▽▲▽▲▽ You are in Dragon Bank! ▽▲▽▲▽▲▽")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►1∙Create new account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►2∙Make Transaction")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►3∙update information of existing account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►4∙removing existing account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►5∙check the details of existing account")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►6∙view customer's list")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print("►7∙exit")
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")

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
    if user_choice == 4:
        account_number = input("account_number_to_delete:")
        delete_account(account_number)

    if user_choice == 5:
        account_number = input("account number: ")
        display_account_information_by_given_account_number(account_number)

    if user_choice == 6:
        display_all_of_the_customers()

    if user_choice == 7:
        quit()


# ─── MAIN ───────────────────────────────────────────────────────────────────────


while True:
    display_menu()


# ────────────────────────────────────────────────────────────────────────────────
