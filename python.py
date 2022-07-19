
from operator import add
import datetime

print("Hello world")  # statement 1 

x = 20  # statement 2
print(x) #statement 3

# two statement in a single line
l = 4 ; w = 5
print("Area of a triangle is:", l * w) #print statement
# implicit continuation
addition = (10+20+
            30+39+33+
            44+93+23)
print(addition)

# To create a list and dictionary

names = ["Arhab" , "Muhammad"]
students = {"Arhab" : 95, "wildan" : 88}
print(names , students.keys())

#return statement

def additions(a ,b):
    return a + b #returns the sum of two numbera

#result is the return value
result = additions(40,50)
print(result)

now = datetime.datetime.now()
print(now)


# print(help("if"))

for i in range(5):
    print(i , end=" ")
    
n = 0
while n < 5:
    print(n , end=" ") 
    n +=  1   
# variables 
nAme = "arhab" #str
age = 25 #int
salary = 258000.60 #float

print(nAme) 
print(age)
print(salary)