
#1 odd or even
a=int(input("enter a number:"))
if a%2==0:
    print("even number")
else:
    print("odd number")

#2 vote eligible
age=int(input("enter age:"))
if age>=18:
    print("eligible for vote")
else:
    print("uneligible for vote")


#3 student pass or fail
mark=int(input("enter mark:"))
if mark>=40:
    print("pass")
else:
    print("fail")

#4 poss or negative
num=int(input("enter a number :"))
if num<=0:
    print("negative")
else:
    print("possitive")


#5 student grade
mark=int(input("enter a mark:"))
if mark>=90:
    print("grade A")
elif 75<=mark<=85:
    print("grade B")
elif 50<=mark<=74:
    print("grade C")
else:
    print("fail")

#6 largest num
a=int(input("enter A:"))
b=int(input("enter B:"))
c=int(input("enter C:"))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")

#7 days
day=int(input("enter a day:"))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
else:
    print("saturday")

#8 arithmetic operation
a=int(input("enter a number:"))
b=int(input("enter a number:"))
operator=input("enter a operator(+,-,*,/):")
if operator=='+':
    print("addition:",a+b)
elif operator=='-':
    print("subtraction:",a-b)
elif operator=='*':
    print("multiple:",a*b)
elif operator=='/':
    print("division:",a/b)

#9 username and password
username=str(input("enter a username:"))
password=int(input("enter a password:"))
if username=="kishore":
    print("username is correct")
else:
    print("invalid username")
    if passoword==2006:
        print("password correct")
    else:
        print("invalid password")
        
#10 traffic signal
colour=str(input("enter a colour:"))
if colour=="red":
    print("stop")
elif colour=="yellow":
    print("get ready")
elif colout=="green":
    print("go")
else:
    print("wait")
