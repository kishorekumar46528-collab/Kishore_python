#Mapping and filter

#1. Double every number in a list.

nums=[1,2,3,4,5]
even=list(map(lambda x:x*2,nums))
print(even)

#2. Find the square of every number.

nums=[1,2,3,4,5]
even=list(map(lambda x:x*2,nums))
print(even)

#3. Add 5 to every number.

nums=[1,2,3,4,5]
even=list(map(lambda x:x+5,nums))
print(even)

#4.Multiply every number by 10.

nums=[1,2,3,4,5]
even=list(map(lambda x:x*10,nums))
print(even)

#5. Convert all names to uppercase.

name=["sharvesh"]
a=list(map(lambda x:x.upper(),name))
print(a)

#6.Get all even numbers.

nums=[1,2,3,4,5]
a=list(filter(lambda x:x%2==0,nums))
print(a)

#7.Get all odd numbers.

nums=[1,2,3,4,5]
a=list(filter(lambda x:x%2!=0,nums))
print(a)

#8.Get numbers greater than 10.

nums=[1,2,3,4,5,12]
a=list(filter(lambda x:x>10,nums))
print(a)

#9.Get numbers less than 50.

nums=[1,2,3,4,5,12]
a=list(filter(lambda x:x<50,nums))
print(a)

#10.Get numbers divisible by 5.

nums=[1,2,3,4,5,12]
a=list(filter(lambda x:x%5==0,nums))
print(a)

#11.Find the cube of every number.

nums=[1,2,3,4,5,12,8]
a=list(map(lambda x:x**3,nums))
print(a)

#12. Find the length of every word in a list.

name=["sharvesh"]
a=list(map(lambda x:len(x),name))
print(a)

#13.Convert temperatures from Celsius to Fahrenheit.

c=[float(input("Enter the celsius:"))]
a=list(map(lambda x:(x*9/5)+32,c))
print(a)

#14.Add 10% to every price in a list.

nums=[1,2,3,4,5,12,8]
a=list(map(lambda x:x*0.1,nums))
print(a)

#15.Convert a list of names into their first-letter uppercase format.

name=["sharvesh","sam","sanjay"]
a=list(map(lambda x:x.capitalize(),name))
print(a)


#16.Get numbers between 10 and 50.

nums=[1,22,32,23,45,12,8,52,82]
a=list(filter(lambda x:10<x<50,nums))
print(a)


#17.Get numbers divisible by both 2 and 3.

nums=[1,22,32,23,45,12,8,52,82]
a=list(filter(lambda x:x%2==0 and x%3==0,nums))
print(a)


#18.Get names starting with "A".

name=["sharvesh","sam","sanjay","Ajay"]
a=list(filter(lambda x:x.startswith("A"),name))
print(a)


#19.Get words having more than 5 characters.

name=["sharvesh","sam","sanjay"]
a=list(filter(lambda x:len(x)>5,name))
print(a)


#20.Get positive numbers from a list.

nums=[-1,22,-32,-23,45,12,8,-52,82]
a=list(filter(lambda x:x>0,nums))
print(a)


#21.Filter even numbers and find their squares.

nums=[1,22,32,23,45,12,8,52,82]
a=list(filter(lambda x:x%2==0,nums))
b=list(map(lambda x:x**2,a))
print(b)

#22. Filter numbers greater than 10 and double them.

nums=[1,22,32,23,45,12,8,52,82]
a=list(filter(lambda x:x>10,nums))
b=list(map(lambda x:x*2,a))
print(b)


#23.Filter names starting with "A" and convert them to uppercase.

name=["sharvesh","sam","sanjay","Ajay"]
a=list(filter(lambda x:x.startswith("A"),name))
b=list(map(lambda x:x.upper(),a))
print(b)


#24.Filter odd numbers and find their cubes.

nums=[1,2,3,4,5]
a=list(filter(lambda x:x%2!=0,nums))
b=list(map(lambda x:x*3,a))
print(b)


#25.Filter words with more than 4 characters and find their lengths.

name=["sharvesh","sam","sanjay"]
a=list(filter(lambda x:len(x)>4,name))
b=list(map(lambda x:len(x),a))
print(b)
