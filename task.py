
'''a=int(input("enter a :"))
b=int(input("enter b:"))
print("add:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a/b)
print("mod:",a%b)
print("floor:",a//b)
print("exp:",a**2)

#average
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
sum=a+b+c
print("average:",sum/3)


#check
a=int(input("enter a:"))
b=int(input("enter b:"))
if a==b:
    print("equal")
elif a>=b:
    print("a is greater")
else:
        print("b is greater")


#simple interest
p=int(input("enter p:"))
t=int(input("enter t:"))
r=int(input("enter r:"))
print("simple interest:",p*r*t/100)
print("compound interest:",p*(1+r/100)**t-p)


#square root
a=int(input("enter a:"))
print("square root:",a**1/2)


#cube root
a=int(input("enter a:"))
print("square root:",a**1/3)


#area and perimeter of rectangle
L=int(input("enter the rectangle Length:"))
B=int(input("enter the rectangle Breadth:"))
print("rectanglearea:",L*B)


#area and perimeter of square
side=int(input("enter a length:"))
area=side*side
perimeter=4*side
print("area of square:",area)
print("primeter of square:",perimeter)


#assignment operation

x=10
x+=5
x-=3
x*=2
x/=4
x%=2
x**=3
print(x)
'''

#user name and password

username=str(input("enter name:"))
password=int(input("enter password:"))
if username==kishore and password==2006:
    print("correct username and password")
    if username==kishore and password!=2006:
        print("correct username but invalid password")
    if username!=kishore and password==2006:
        print("correct password but invalid username")
    else:
        print("incorrect username and password")



    
