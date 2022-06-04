

# ─── IMPORTS ────────────────────────────────────────────────────────────────────

import math
import json
import os
import random
from datetime import datetime
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
    f = open(FILE_PATH, "r")
    data = f.read()
    return json.loads(data)


def set_data(data):
    """
    Writes the bank information into the data file
    """
    f = open(FILE_PATH, "w")
    f.write(json.dumps(data))


def get_users_as_list():
    """
    This functions loadst the user data and converts it
    from a dictionary to a list and then appends the
    account_number as a key from outside into the the
    data object.
    """
    result = []
    users = get_data()
    for user_account_number in users:
        user_data = users[user_account_number]
        user_data["account_number"] = user_account_number
        result.append(user_data)
    return result


# ─── LINKED LIST ────────────────────────────────────────────────────────────────


class LinkedList:
    """
    A Linked List Node
    """

    def __init__(self, _value, _next):
        """
        Creates the node with a value and reference to
        the next object
        """
        self.value = _value
        self.next = _next

    def index(self, n):
        """
        Similar to A[i], this works as A.index(i)
        """
        if n == 0:
            return self.value
        else:
            if self.next == None:
                return None
            else:
                return self.next.index(n - 1)

    def size(self):
        """
        Similar to len(A), this is A.size()
        """
        if self.next == None:
            return 1
        else:
            return 1 + self.next.size()


# ─── HEAP SORT ──────────────────────────────────────────────────────────────────


def heap_sort(input_list, field):
    """
    A custom implementation of the heap sort function that
    also gets a field and then assuems the input_list contains
    data objects. So it sorts based on a common key on all those
    functions. This makes possible to sort users based on different
    aspects, like based on full name or phone number
    """
    range_start = int((len(input_list)-2)/2)
    for start in range(range_start, -1, -1):
        sift_down(input_list, field, start, len(input_list)-1)

    range_start = int(len(input_list)-1)
    for end_index in range(range_start, 0, -1):
        swap(input_list, end_index, 0)
        sift_down(input_list, field, 0, end_index - 1)
    return input_list


def swap(input_list, a, b):
    """
    Swaps two elements of a list with the python shorthand
    """
    input_list[a], input_list[b] = input_list[b], input_list[a]


def sift_down(input_list, field, start_index, end_index):
    """
    The "Stif Down" function of the heap sort algorithm,
    customized to also include object fields.
    """
    root_index = start_index
    while True:
        child = root_index * 2 + 1
        if child > end_index:
            break
        if child + 1 <= end_index and input_list[child][field] < input_list[child + 1][field]:
            child += 1
        if input_list[root_index][field] < input_list[child][field]:
            swap(input_list, child, root_index)
            root_index = child
        else:
            break


# ─── BINARY SEARCH ──────────────────────────────────────────────────────────────


def text_binary_search(input_list, field, query):
    """
    A custom binary search implementation that:
    (1) Assumes the input_list to have elements of type object
        and then sorts by a common key in all those abjects name
        "field"
    (2) Lowercases and trims the text in the fields
        so for example "foo bar" can match "FooBar"
    """
    low = 0
    high = len(input_list) - 1
    query = make_text_searchable(query)
    while low <= high:
        mid = math.floor((low + high) / 2)
        if make_text_searchable(input_list[mid][field]) > query:
            high = mid - 1
        elif make_text_searchable(input_list[mid][field]) < query:
            low = mid + 1
        else:
            return mid
    return -1


def make_text_searchable(text):
    """
    Lowercases the text and removes spaces
    """
    return text.lower().replace(" ", "")


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


# ─── update information ──────────────────────────────────────────────────────────


def update_information(account_number):
    """
    Given an account number, this asks the user what to change and then
    changes the properties of that.
    """
    users = get_data()
    print_horizonal_line()
    print("► 1 ∙ Full Name ")
    print_horizonal_line()
    print("► 2 ∙ Gender ")
    print_horizonal_line()
    print("► 3 ∙ City ")
    print_horizonal_line()
    print("► 4 ∙ Phone Number ")
    print_horizonal_line()
    command = int(input("What to change? "))
    print_horizonal_line()
    if command == 1:
        new_name = input("New Full Name: ")
        users[account_number]["full_name"] = new_name
    if command == 2:
        new_gender = input("New Gender: ")
        users[account_number]["gender"] = new_gender
    if command == 3:
        new_city = input("New City: ")
        users[account_number]["city"] = new_city
    if command == 4:
        new_phone_number = input("New Phone Number: ")
        users[account_number]["phone_number"] = new_phone_number

    set_data(users)
    clean_terminal_screen()
    display_account_information_by_given_account_number(account_number)


# ─── CREATE A NEW USER ──────────────────────────────────────────────────────────


def create_new_user(full_name, balance, gender, city, phone_number):
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
        "account_creation_date": date,
        "city": city,
        "phone_number": phone_number
    }
    set_data(users)
    display_account_information_by_given_account_number(account_number)


# ─── SEARCH ACCOUNT ─────────────────────────────────────────────────────────────


def search_account(field, query):
    """
    Searches the "query" from the user data in the "field" fields
    """
    users = get_users_as_list()
    users = heap_sort(users, field)
    index = text_binary_search(users, field, query)
    if index == -1:
        print("──── Error ──────────────────────────────────")
        print("Found no one as", query)
    else:
        user = users[index]
        display_user_object(user, user["account_number"])


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


# ─── INTERFACE TOOLS ────────────────────────────────────────────────────────────


def clean_terminal_screen():
    """
    Cleans the terminal screen by performing a system
    clear command. Cls on windows and Clear on UNIX ones.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_horizonal_line():
    """
    A pretty decorative horoizontal line.
    """
    print("─────────────────────────────────────────────")


# ─── DISPLAY USER OBJECT ────────────────────────────────────────────────────────


def display_account_information_by_given_account_number(account_number):
    """
    Diplays the information about a given account number
    """
    users = get_data()
    user = users[account_number]
    display_user_object(user, account_number)


def display_user_object(user_object, account_number):
    """
    Displays a single user object. The account_number is taken
    separately since there can be either a list input or a dictiory
    input. In a list input the account_number is within the user object
    and in the dictionary form the account_number is the key mapped
    to the dictionary
    """
    print_horizonal_line()
    print("Full name:      ", user_object["full_name"])
    print("Account number: ", account_number)
    print("Created at:     ", user_object["account_creation_date"])
    print("Balance:        ", user_object["balance"])
    print("Gender:         ", user_object["gender"])
    print("City:           ", user_object["city"])
    print("Phone:          ", user_object["phone_number"])


def display_all_accounts_sorted_by(field):
    """
    Displays all the users one after the other, sorted by a given field
    """
    users = get_users_as_list()
    users = heap_sort(users, field)
    clean_terminal_screen()
    for user in users:
        display_user_object(user, user["account_number"])


# ─── DISPLAY USER DATA MENU ─────────────────────────────────────────────────────


def ask_user_what_field_to_sort_the_display_by():
    """
    Shows a menu so that the user cas pick a field to sort the data by.
    """
    print("Sorting by:")
    print_horizonal_line()
    print("► 1 ∙ Full Name ")
    print_horizonal_line()
    print("► 2 ∙ Gender ")
    print_horizonal_line()
    print("► 3 ∙ City ")
    print_horizonal_line()
    print("► 4 ∙ Phone Number ")
    print_horizonal_line()
    print("► 5 ∙ Account Creating Date ")
    print_horizonal_line()
    print("► 6 ∙ Account Number ")
    print()
    command = input("Your option: ")
    if command == "1":
        return "full_name"
    if command == "2":
        return "gender"
    if command == "3":
        return "city"
    if command == "4":
        return "phone_number"
    if command == "5":
        return "account_creation_date"
    if command == "6":
        return "account_number"
    return "full_name"


# ─── DISPLAY MENU ───────────────────────────────────────────────────────────────


def display_menu():
    """
    Displays the welcome menu and asks the user for a
    command to perform (which then performs).

    This also acts as the UI and recieves the information
    regarding of the respective functions.
    """
    clean_terminal_screen()

    print("               ＄ WELCOME ＄")
    print("   ▽▲▽▲▽▲▽ You Are in Dragon Bank! ▽▲▽▲▽▲▽")
    print_horizonal_line()
    print("► 1 ∙ Create New Account")
    print_horizonal_line()
    print("► 2 ∙ Make Transaction")
    print_horizonal_line()
    print("► 3 ∙ Update information of Existing Account")
    print_horizonal_line()
    print("► 4 ∙ Removing Existing Account")
    print_horizonal_line()
    print("► 5 ∙ Search Account")
    print_horizonal_line()
    print("► 6 ∙ View Customer's List")
    print_horizonal_line()
    print("► 7 ∙ Exit")
    print_horizonal_line()

    user_choice = int(input("☞ Enter your command: "))

    clean_terminal_screen()

    if user_choice == 1:
        print("── Creating a new user ──────────────────────")
        user_name = input("Full Name: ")
        balance = float(input("Balance: "))
        gender = input("Gender: ")
        city = input("City of Residence: ")
        phone_number = input("Phone Number: ")
        create_new_user(user_name, balance, gender, city, phone_number)

    if user_choice == 2:
        print("── Requesting Transaction ───────────────────")
        sender = input("Sender's Account Number: ")
        receiver = input("Recipient's Account Number: ")
        amount = float(input("Transaction Amount: "))
        perform_transaction(sender, receiver, amount)

    if user_choice == 3:
        print("── Changing Account Information ─────────────")
        account_number = input("Account Number To Change: ")
        update_information(account_number)

    if user_choice == 4:
        print("── Deleting an Account ──────────────────────")
        account_number = input("Account number to delete: ")
        delete_account(account_number)

    if user_choice == 5:
        print("── Search Account ───────────────────────────")
        query = input("Searching for: ")
        clean_terminal_screen()
        search_account("full_name", query)

    if user_choice == 6:
        print("── Displaying all Accounts ──────────────────")
        field = ask_user_what_field_to_sort_the_display_by()
        display_all_accounts_sorted_by(field)

    if user_choice == 7:
        quit()

    print()
    print_horizonal_line()
    input("PRESS ENTER TO CONTINUE ")
    print()


# ─── MAIN ───────────────────────────────────────────────────────────────────────


while True:
    display_menu()


# ────────────────────────────────────────────────────────────────────────────────
