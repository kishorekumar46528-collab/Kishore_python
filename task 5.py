# User define function
1.
'''def hii():
    print("hello word!")
hii()

2.
n=str(input("enter your name:"))
def name(n):
    print(n)
name(n) 

3.
def add(a,b):
    print(a+b)
add(5,5) 

4.
def sub(a,b):
    print(a-b)
sub(10,5) 

5.
def square(a):
    print(a**2)
square(5) 

6.
n=int(input("enter a number:"))
def even(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
even(n) 

7.
def largest(a,b):
    if a>b:
        print("a is largest")
    else:
        print("b is larget")
largest(10,5) 

8.
l=int(input("enter l:"))
b=int(input("enter b:"))
def rectangle(l,b):
    print(l*b)
rectangle(6,5) 

9.
def factorial(n):
    print(n-1)
    if n==0:
        return
factorial(5) 

10.
n=int(input("enter a number:"))
def number(n):
    if n<0:
        print("negative")
    elif n>0:
        print("positive")
    else:
        print("zero")
number(n) 

#Recursive function

11.
def number(n):
    if n>5:
        return
    print(n)
    number(n+1)
number(1) 

12.
def number(n):
    if n<1:
        return
    print(n)
    number(n-1)
number(5) 

13.
def number(n):
    print(n*(n-1))
number(5) 

14.
def sum(n):
    if n<=0:
        return 0
    return n+sum(n-1)

print(sum(5)) 

15.
def square(n):
    if n<0:
        n=-n
    if n==0:
        return 0
    return square(n-1)+2*n-1
print(square(3))
print(square(-4)) 

#Lambda function

16.
square=lambda x: x**2
print(square(3))
print(square(-6)) 

17.
cube=lambda x: x**3
print(cube(2))
print(cube(3)) 

18.
add=lambda x,y:x+y
print(add(5,5))
print(add(6,6)) 

19.
n=int(input("enter a number:"))
n=lambda n:"even" if n%2==0 else "odd" 

20.
largest=lambda a,b: a if a>b else b
print(largest(12,25))
print(largest(50,40)) 

#build in function

21.
txt="kishore"
print(len(txt)) 

22.
numbers=[4,12,3,98,24]
result=max(numbers)
print(result) 

23.
numbers=[4,12,3,98,24]
result=min(numbers)
print(result) 

24.
numbers=[4,12,3,98,24]
result=sum(numbers)
print(result) '''











































