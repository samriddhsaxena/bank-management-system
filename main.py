import json
import random
import string
import pathlib as Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No data found")
    except Exception as e:
        print(f"Error: {e}")

    @classmethod
    def __update(cls):
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createAccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your pin: ")),
            "accountNo": Bank.__accountGenerate(),
            "balance": 0
        }
        if info["age"] < 18 or len(str(info["pin"]))!=4:
            print("You are not eligible to open an account")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please note down your account number")
            Bank.data.append(info)

            Bank.__update()

    def depositMoney(self):
        accNum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i["accountNo"]==accNum and i["pin"]==pin]
    
        if userdata == False:
            print("Invalid account number or pin")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("Invalid amount")
            else:
                userdata["balance"] += amount
                Bank.__update()
                print("Money has been deposited successfully")

user = Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing money in account")
print("Press 3 for withdrawing money from account")
print("Press 4 for viewing details")
print("Press 5 for updating details")
print("Press 6 for deleting your account")

check = int(input("Enter your choice: "))

if check == 1:
    user.createAccount()

elif check == 2:
    user.depositMoney()

