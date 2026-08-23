#BEGINNER TASK
'''
1.
for i in range(1,11):
    print(i)

2.
for i in range(10,0,-1):
    print(i)

3.
for i in range(1,21):
    if i%2==0:
        print("even number:",i)

4.
for i in range(1,21):
    if i%2!=0:
        print("odd number:",i)

5.
num=5
for i in range(1,11):
    print("multiple:",num*i)

6.
sum=0
for i in range(1,101):
    sum=sum+i
    print("sum=",sum)

7.
sum=0
for i in range(1,51):
    if i%2==0:
        sum=sum+i
        print("sum=",sum)

8.
A="PYTHON"
for i in A:
    print(i)

9.
num=0
for i in range(1,11):
    num=i*2
    print("number:",num)


#intermediate task

1.
text="Hello world"
vowels="aeiouAEIOU"
count=0
for i in text:
    if i in vowels:
        count +=1
        print("no of vowels:", count) 

2.
sum=0
for num in range(1,101):
    if num%2==0:
        sum+=num
        print("sum even numbers:",sum) 

3.
num=5
factorial=1
for i in range(1,num+1):
    factorial*=i
    print("output:",factorial) 

4.
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime") 

5.
for n in range(2,101):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print(n,"prime")

6.
num=[10,45,23,89,12,67]
largest=num[0]
for i in num:
    if i>largest:
        largest=i
print("largest number:",largest) 


7.
numbers=[10,-45,23,-89,12,-67,0]
positive_count=0
negative_count=0
for i in numbers:
    if i>0:
        positive_count+=1
    elif i<0:
        negative_count+=1
print("positive numbers:",positive_count)
print("negative numbers:",negative_count) 

8.
text="PYTHON"
reversed=""
for i in text:
    reversed=i+reversed
print("Input:",text)
print("Output:",reversed) '''

9.
text=input("enter a string:")
char=input("enter a character:")
count=0
for i in text:
    if i==char:
        count+=1
print("character appears",count,"times")





