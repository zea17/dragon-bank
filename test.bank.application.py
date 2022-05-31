from datetime import datetime
import random
users = {}

def AccountNumber():
    prefix = "17172424"
    result = ""
    for i in (0,8):
        random_number = random.randint(1, 9)
        result += str(random_number)
    
    return prefix + result


def transaction(sender,receiver,amount):
    if sender in users and receiver in users:
        if users[sender]["balance"] >= amount:
            users[sender]["balance"] -= amount
            users[receiver]["balance"] += amount


def create_new_user(user_name, BALANCE):
    date = datetime.today().strftime('%Y-%m-%d')
    users[user_name] = {
       
        "account_number": AccountNumber(),
        "balance": BALANCE,
        "Account_creation_date": date
    }


print(create_new_user("zea",100))
print(create_new_user("pou",180))
print(transaction("pou","zea",20))
print(users)