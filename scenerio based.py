'''#ATM withdraw
amount=int(input("enter amount:"))
balance=4000
if amount<=balance:
    print("amount withdraw")
else:
    print("insufficient balance") 

#login system
user=str(input("enter a name:"))
password=2006
if user=="kishore":
    if password==2006:
        print("login successful")
    else:
        print("wrong password")
else:
    print("incorrect user") 

#online shopping
amount=int(input("enter a amount:"))
purchase=5000
if amount>=5000:
    print("20% discount")
else:
    print("no discount") 

#student result
mark=int(input("enter a mark:"))
if mark>=90:
    print("A grade")
elif 75>mark<89:
    print("B grade")
elif 64>mark<74:
    print("C grade")
else:
    print("Fail") 

#password attempt
correct_password="2006"
for i in range(3):
    password=int(input("enter a password:"))
    if password==correct_password:
        print("login successful")
        break
    else:
        print("wrong password") 

#ATM menu

while True:
    print("1. balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.exist")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("balance")
        break
    elif choice==2:
        print("withdraw")
        break
    elif choice==3:
        print("deposit")
        break
    else:
        print("exist")
        break 

#shopping cart
products=["laptop","mouse","keyboard","out of stock"]
for product in products:
    if product=="out of stock":
        continue
    print(product) 

#parking system
vehicles=["TN30ABC","TN40BCD","TN30EFG"]
for vehicle in vehicles:
    if vehicles=="TN40BCD":
        print("vehicle found")
        break 

#email validation
emails=["k@gmail.com","I@gmail.com","Sgmail.com"]
for email in emails:
    if "@" not in email:
        continue
    else:
        print("email validation",email) 

#searching number
for i in range(1,101):
    if i ==75:
        print("number found")
        break 

#loan eligible
age=int(input("enter age:"))
salary=int(input("enter salary:"))
if age>=21:
    if salary>=30000:
        print("loan approved")
    else:
        print("loan not approved")
else:
    print("loan not approved") 

#college addmission
mark=75
document=True
if mark>=60:
    if document==True:
        print("addmission approved")
    else:
        print("addmission not approved")
else:
    print("addmission not approved") '''


        



















































