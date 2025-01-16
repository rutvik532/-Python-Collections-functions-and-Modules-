"""Accessing List
Theory: 
• Understanding how to create and access elements in a list. 
--->mylist=[1,2,3,"python",'Rutvik',16.50]
    print(mylist)
    for i in mylist :
        print(i)

• Indexing in lists (positive and negative indexing). 
--->We can access the list by index and the print the element by index and positive index start from 0 and until the number of element
to minus one number to print all element.
--->in negetive index start from number of element of minus number to minus one number to access all element.
• Slicing a list: accessing a range of elements.
--->in the list slicing for example we have mylist=[1,2,3,"python",'Rutvik',16.50] this list and print or create another list from we  are choice 
    like from 1 element to 3 element so writte print(mylist[1:4]) and if we have to print like even element so print(mylist[1:3:2])so in this 
    last 2 is jump in element is this jump by 2 element.

#Lab: 
#• Write a Python program to create a list with elements of multiple data types (integers, 
#strings, floats, etc.). 
mylist=[1,2,3,"python",'Rutvik',16.50]
print(mylist)
#• Write a Python program to access elements at different index positions.
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])
#Practical Examples: 
#1. Write a Python program to create a list of multiple data type elements. 
mylist=[1,2,3,"python",'Rutvik',16.50]
# 2. Write a Python program to find the length of a list using the len() function. 
c=len(mylist)
print("Lenght of list:",c)

#2. List Operations
Theory: 
• Common list operations: concatenation, repetition, membership. 
concatenation
mylist1=[1,2,3,4,5]
mylist2=[6,7,8,9]
result=mylist1+mylist2
print(result)
repetition
result=mylist2*2
membership
print(2 in mylist2)
print(6 not in mylist2)

• Understanding list methods like append(), insert(), remove(), pop().
mylist1=[1,2,3,4,5]
mylist1.append("python")
mylist1.insert("C",3)
mylist1.remove("python")
mylist1.pop()
mylist1.pop(2)

#Lab: 
#• Write a Python program to add elements to a list using insert() and append(). 
mylist1=[1,2,3,4,5]
mylist1.append("python")
print(mylist1)
mylist1.insert(3,2)
print(mylist1)
#• Write a Python program to remove elements from a list using pop() and remove(). 
mylist1=[1,2,3,4,5,"python"]
mylist1.remove("python")
print(mylist1)
mylist1.pop()
print(mylist1)
mylist1.pop(2)
print(mylist1)

#Theory: 
#• Iterating over a list using loops. 
mylist1=[1,2,3,4,5,"python"]
for i in mylist1 :
    print(i)
#• Sorting and reversing a list using sort(), sorted(), and reverse(). 
mylist1=[2,6,4,7,8,4,9]
mylist1.sort()
print(mylist1)
mylist3=[1,2,3,4,5,6]
mylist3.reverse()
print(mylist3)



#• Basic list manipulations: addition, deletion, updating, and slicing. 
mylist1=[2,6,4,7,8,4,9]
mylist3=[1,2,3,4,5,6]
result=mylist1+mylist3


print(result)
print(mylist1.remove(2))

mylist1.append("python")
print(mylist1)
print(mylist1[1:3])
print(mylist1[-8:-1])

#Lab: 
#• Write a Python program to iterate over a list using a for loop. 
mylist1=[1,2,3,4,5,"python",16.50]
for i in mylist1 :
    print(i)
#• Write a Python program to sort a list using both sort() and sorted().
mylist1=[2,6,4,7,8,4,9]
mylist1.sort()
print(mylist1)
#Practical Examples: 5) 
#Write a Python program to iterate through a list and print each element.
mylist1=[1,2,3,4,5,"python",16.50]
for i in mylist1 :
     print(i)
#6) Write a Python program to insert elements into an empty list using a for loop and append().
mylist=[]
n=int(input("Enter how many element you have to enter!!"))
for i in range(n) :
    a=input("Enter Element:")
    mylist.append(a)

print(mylist)

4#. Tuple 
#Theory: 
#• Introduction to tuples, immutability. 
tuple is collection of group of element by ordered collection
we can not change or update any element or index in tuple
#• Creating and accessing elements in a tuple. 
mytuple=(1,2,3,4,5,"python","c")
for i in mytuple :
    print(i)
#• Basic operations with tuples: concatenation, repetition, membership. 
mytuple=(1,2,3,4,5,"python","c")
mytuple1=(4,6,8,9)
result=mytuple+mytuple1
print(result)
result1=mytuple*2
print(result1)
mytuple=(1,2,3,4,5,"python","c")
print(2 in mytuple)
print(6 in mytuple)
#Lab: 
# Write a Python program to create a tuple with multiple data types. 
mytuple=(1,2,3,4,5,"python","c",12.5,16.54)
print(mytuple)
#• Write a Python program to concatenate two tuples. 
mytuple=(1,2,3,4,5,"python","c")
mytuple1=(4,6,8,9)
result=mytuple+mytuple1
print(result)

#Practical Examples:
#7) Write a Python program to convert a list into a tuple. 
mylist1=[1,2,3,4,5,"python",16.50]
mytuple=tuple(mylist1)
print(mytuple)
#8) Write a Python program to create a tuple with multiple data types. 
mytuple=(1,2,3,4,5,"python",16.50)
print(mytuple)
#9) Write a Python program to concatenate two tuples into one. 1
mytuple=(1,2,3,4,5,"python","c")
mytuple1=(4,6,8,9)
result=mytuple+mytuple1
print(result)
#10) Write a Python program to access the value of the first index in a tuple
mytuple=(1,2,3,4,5,"python","c")
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[3])
print(mytuple[4])
print(mytuple[5])
print(mytuple[6])

#5. Accessing Tuples 
#Theory: 
#• Accessing tuple elements using positive and negative indexing. 
mytuple=(1,2,3,4,5,"python","c")
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[3])
print(mytuple[4])
print(mytuple[5])
print(mytuple[6])

#• Slicing a tuple to access ranges of elements. 
mytuple=(1,2,3,4,5,"python","c")
print(mytuple[1:8])
print(mytuple[1:5])
print(mytuple[-8:-1])
print(mytuple[-6:-4])

#Lab: 
#• Write a Python program to access values between index 1 and 5 in a tuple. 
mytuple=(1,2,3,4,5,"python","c")
print(mytuple[1:5])
#• Write a Python program to access alternate values between index 1 and 5 in a tuple. 
mytuple=(1,2,3,4,5,"python","c")
print(mytuple[1:8:2])
#Practical Examples: 11) Write a Python program to access values between index 1 and 5 in a tuple. 
mytuple=(1,2,3,4,5,"python","c")
print(mytuple[1:5])
#12) Write a Python program to access the value from the last index in a tuple.
mytuple=(1,2,3,4,5,"python","c")
print(mytuple[::-1])
6. Dictionaries 
Theory: 
#• Introduction to dictionaries: key-value pairs.
# -->in the dictinories we have a two pair key and values we can update the values but the key is unique so we cant change or update in key 
#• Accessing, adding, updating, and deleting dictionary elements.
# -->
my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A"} 
my_dict1={"name":"pradip","Roll_no.":2,"Grade":"A"}
c=my_dict | my_dict1
#print(my_dict.items())
my_dict.update(my_dict1)
print(my_dict)
my_dict["Mark"]=35
print(my_dict)
my_dict.pop("name")
print(my_dict)
#• Dictionary methods like keys(), values(), and items(). 
my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A"} 
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
#Lab: 
#• Write a Python program to create a dictionary with 6 key-value pairs. 
my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A","Age":22,"Overall_mark":200,"percentage":88} 
print(my_dict)
#• Write a Python program to access values using dictionary keys. 

my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A"} 
print(my_dict.keys())
#Practical Examples: 13) Write a Python program to create a dictionary of 6 key-value pairs. 
my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A","Age":22,"Overall_mark":200,"percentage":88} 
print(my_dict.items())
#14) Write a Python program to access values using keys from a dictionary.
my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A","Age":22,"Overall_mark":200,"percentage":88} 
print(my_dict.values())
print(my_dict.items())


#. Working with Dictionaries 
#Theory: 
#• Iterating over a dictionary using loops. 
my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A","Age":22,"Overall_mark":200,"percentage":88} 
for i,v in my_dict.items() :
    print(i,v)
#• Merging two lists into a dictionary using loops or zip(). 
list11=["name","age","Roll_no.","city"]
list2=["Rutvik",22,1,"Germany"]
my_dict={}
for i in range(len(list11)) :
    my_dict[list11[i]]=list2[i]

print(my_dict)
#Lab: 
#• Write a Python program to update a value in a dictionary. 
my_dict={'name': 'Rutvik', 'age': 22, 'Roll_no.': 1, 'city': 'Germany'}
my_dict["name"]="pradip"
print(my_dict)
#• Write a Python program to merge two lists into one dictionary using a loop. 
list11=["name","age","Roll_no.","city"]
list2=["Rutvik",22,1,"Germany"]
my_dict={}
for i in range(len(list11)) :
    my_dict[list11[i]]=list2[i]

print(my_dict)

#Practical Examples: 15) Write a Python program to update a value at a particular key in a 
#dictionary. 
my_dict={'name': 'Rutvik', 'age': 22, 'Roll_no.': 1, 'city': 'Germany'}
my_dict["name"]="pradip"
# 16) Write a Python program to separate keys and values from a dictionary using 
#keys() and values() methods. 
my_dict={"name":"Rutvik","Roll_no.":1,"Grade":"A","Age":22,"Overall_mark":200,"percentage":88} 
print(my_dict.keys())
print(my_dict.values())
# 17) Write a Python program to convert two lists into one 
#dictionary using a for loop. 
list11=["name","age","Roll_no.","city"]
list2=["Rutvik",22,1,"Germany"]
my_dict={}
for i in range(len(list11)) :
    my_dict[list11[i]]=list2[i]

print(my_dict)
#8. Functions 
#Theory: 
#• Defining functions in Python. 
def sum(a,b) :
    print("Addition:",a+b)

c=int(input("Enter a number for summation:"))
d=int(input("Enter a number for summation:"))
sum(c,d)

#• Different types of functions: with/without parameters, with/without return values. 
#-->with parameter without return
def sum(a,b) :
    print("Addition:",a+b)

c=int(input("Enter a number for summation:"))
d=int(input("Enter a number for summation:"))
sum(c,d)
#without parameter without return
def sum() :
    a=int(input("Enter a number for summation:"))
    b=int(input("Enter a number for summation:"))
    print("Addition:",a+b)


sum()
#with parameter with return
def sum(a,b) :
    return "Addition:",a+b

c=int(input("Enter a number for summation:"))
d=int(input("Enter a number for summation:"))
e=sum(c,d)
print(e)
#without parameter with return
def sum() :
    a=int(input("Enter a number for summation:"))
    b=int(input("Enter a number for summation:"))
    return a+b


e=sum()

print("Addition:",e)

#• Anonymous functions (lambda functions). 
a= lambda x,y : x+y 

result=a(5,7)
print("Addition of two number:",result)

#Lab: 
#• Write a Python program to create a function that takes a string as input and prints it. 
def sum(a) :
    print("input string:",a)

c=input("Enter a number for summation:")
sum(c)
#• Write a Python program to create a calculator using functions. 
def add(a,b) :
    print("Addition:",a+b)

def sub(c,d) :
    print("Substraction:",c-d)

def mul(d,e) :
    print("Multiploication:",d*e)

def div(f,g) :
    print("Division:",f/g)


print("press 1 for Addition:")
print("press 2 for Substraction:")
print("press 3 for Multiplication:")
print("press 4 for Division:")

choice=int(input("Enter your choice:"))

if choice ==1 :
    a=int(input("Enter a number for Addition:"))
    b=int(input("Enter a number for Addition:"))
    add(a,b)
elif choice ==2 :
    c=int(input("Enter a number for Substraction:"))
    d=int(input("Enter a number for Substraction:"))
    sub(c,d)
elif choice ==3 :
    a=int(input("Enter a number for Addition:"))
    b=int(input("Enter a number for Addition:"))
    mul(d,e)
elif choice ==4 :
    f=int(input("Enter a number for Division:"))
    g=int(input("Enter a number for Division:"))
    div(f,g)
else :
    print("Invalid choice!!!")
    

#Practical Examples: 19) Write a Python program to print a string using a function. 
def sum(a) :
    print("input string:",a)

c=input("Enter a number for summation:")
sum(c)
#20) Write a Python program to create a parameterized function that takes two arguments and prints their sum.
def sum(a,b) :
    return "Addition:",a+b

c=int(input("Enter a number for summation:"))
d=int(input("Enter a number for summation:"))
e=sum(c,d)
print(e)
#without parameter with return
def sum() :
    a=int(input("Enter a number for summation:"))
    b=int(input("Enter a number for summation:"))
    return a+b


e=sum()

print("Addition:",e)
#21) Write a Python program to create a lambda function with one expression. 
result=lambda x,y:x+y

x=int(input("Enter Number for character:"))
y=int(input("Enter Number for character:"))

c=result(x,y)
print("Addition:",c)
# 22) Write a Python program to create a lambda function with two expressions.
result=lambda x,y:(x+y,x*y)

x=int(input("Enter Number for character:"))
y=int(input("Enter Number for character:"))

c,d=result(x,y)
print("Addition:",c)
print("multiplication:",d)

#9. Modules 
#Theory: 
#• Introduction to Python modules and importing modules. 
#-->A module in Python is a file containing Python code (functions, classes, and variables) that you can use in other 
# Python programs. It helps organize code into reusable and manageable parts.
#• Standard library modules: math, random. 
#-->we can import of math module to find the some shortcut (e.g.sqrt() to find the squareroot,ceil to find the float number uper value)
#• Creating custom modules. 
#-->for example we have one module my_module and another one is my_class and we have to use my_module to my_class spo we can import my_
#module to my_class to access my_module to my_class
#Lab: 
#• Write a Python program to import the math module and use functions like sqrt(), ceil(), 
#floor(). 
import math
n=int(input("Enter the number for squareroot(integer numebr):"))
o=float(input("Enter the number for :"))

print(math.sqrt(n))
print(math.ceil(o))
print(math.floor(o))
#• Write a Python program to generate random numbers using the random module. 

import random

print(random.random())
print(random.randint(1000,2000))
print(random.choices([5,6,7,8,9]))
#Practical Examples: 23) Write a Python program to demonstrate the use of functions from the math module.
n=int(input("Enter the number for squareroot(integer numebr):"))
o=float(input("Enter the number for :"))

print(math.sqrt(n))
print(math.ceil(o))
print(math.floor(o))
#24) Write a Python program to generate random numbers between 1 and 100 using the random module.
import random

print(random.randint(1,100))"""
