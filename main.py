import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            data = []
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
    
        if not userdata:
            print("Invalid account number or pin")
            return
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000 or amount <= 0:
                print("Invalid amount")
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print("Money has been deposited successfully")
    
    def withdrawMoney(self):
        accNum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i["accountNo"]==accNum and i["pin"]==pin]
    
        if not userdata:
            print("Invalid account number or pin")
            return
        else:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > userdata[0]["balance"] or amount < 0:
                print("Invalid amount")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print("Money has been withdrawn successfully")
    def showdetails(self):

        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        print("your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
    
    def updatedetails(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Invalid account number or pin")
            return
        
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name or press enter : "),
                "email":input("please tell your new Email or press enter to skip :"),
                "pin": input("enter new Pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")
    
    def Delete(self):
        accNum = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i["accountNo"]==accNum and i["pin"]==pin]
    
        if not userdata:
            print("Invalid account number or pin")
            return
        else:
            check = input("Are you sure you want to delete your account? (y/n): ")
            if check == "y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Account has been deleted successfully")
            else:
                print("Account has not been deleted")

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

elif check == 3:
    user.withdrawMoney()

elif check == 4:
    user.showdetails()

elif check == 5:
    user.updatedetails()

elif check==6:
    user.Delete()

#   MADE WITH LOVE BY SAMRIDDH SAXENA