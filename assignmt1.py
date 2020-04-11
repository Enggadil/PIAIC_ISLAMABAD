#!/usr/bin/env python
# coding: utf-8
1. Calculate Area of a Circle
Write a Python program which accepts the radius of a circle from the user and compute the area.
Program Console Sample Output 1:
Input Radius: 0.5
Area of Circle with radius 0.5 is 0.7853981634
# In[3]:


from math import pi
radius=float(input("please enter radius"))
area=2*pi**radius
print("the area is "+str(area))

2. Check Number either positive, negative or zero
Write a Python program to check if a number is positive, negative or zero
Program Console Sample Output 1:
Enter Number: -1
Negative Number Entered
Program Console Sample Output 2:
Integer: 3
Positive Number Entered
Program Console Sample Output 3:
Integer: 0
Zero Entered
# In[10]:


num=int(input("please enter number"))
if num>0:
    print("pasitive number entered")
elif num<0:
    print("negative number entered")
else:
    print("zero entered")

Write a Python program to check whether a number is completely divisible by another number. Accept two integer
values form the user
Program Console Sample Output 1:
Enter numerator: 4
Enter Denominator: 2
Number 4 is Completely divisible by 2
Program Console Sample Output 2:
Enter numerator: 7
Enter Denominator: 4
Number 7 is not Completely divisible by 4

# In[19]:


numerator=float(input("please Enter numerator:"))
denominator=float(input("please Enter Denominator: "))
if (numerator%denominator==0):
    print("number "+str(numerator)+" is completely divisible by "+ str(denominator))
    
else:
     print("number "+str(numerator)+" is  not completely divisible by "+ str(denominator))

4. Days Calculator
Write a Python program to calculate number of days between two dates
Program Console Output:
Enter a date in (dd/mm/yy) format: 12/12/2018
Enter a date in (dd/mm/yy) format: 16/12/2018
There are 4 days in between 12/12/2018 and 16/12/18
# In[21]:



from datetime import date
f_date=date(2014,7,7)
l_date=date(2016,8,9)
days=l_date-f_date
print(days)

5. Calculate Volume of a sphere
Write a Python program to get the volume of a sphere, please take the radius as input from user
Program Console Output:
Enter Radius of Sphere: 1
Volume of the Sphere with Radius 1 is 4.18
# In[22]:


from math import pi
radius=float(input("please enter radius:"))
volume=4*pi*radius
print("volume of the sphere with radius  "+str(radius)+" is "+str(volume))

Copy string n times
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
Program Console Output:
Enter String: Hi
How many copies of String y
# In[23]:


st=input("please enter string :")
n=int(input("please enter value for n :"))
result=n*st
print(result)

7. Check if number is Even or Odd
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an
appropriate message to the user
Program Console Output 1:
Enter Number: 4
4 is Even
Program Console Output 2:
Enter Number: 9
9 is Odd
# In[24]:


num=int(input("please enter number for check:"))
if num%2==0:
    print("the enter number is even")
else:
    print("the enter number is odd")

8. Vowel Tester
Write a Python program to test whether a passed letter is a vowel or not
Program Console Output 1:
Enter a character: A
Letter A is Vowel
Program Console Output 2:
Enter a character: e
Letter e is Vowel
Program Console Output 2:
Enter a character: N
Letter N is not Vowel
# In[30]:


char=input("please enter your character:")
l=['a','e','i','o','u','A','I','O','E','U']
for i  in l:
    if char==l:
        print("latter "+ " "+char +"is vowel")
        break
    else:
        print("latter "+ " "+char +"is vowel")  


# In[31]:


l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l)

Triangle area
Write a Python program that will accept the base and height of a triangle and compute the area
Program Console Sample 1:
Enter magnitude of Triangle base: 4
Enter Magnitude of Triangle Height: 4
Area of a Triangle with Height 4 and Base 4 is 8
# In[1]:


base=float(input("please Enter magnitude of Triangle base:"))
height=float(input("please Enter Magnitude of Triangle Height:"))
area=base*height
print("Area of a Triangle with Height"+ " "+str(height)+" " +"and" +str(base) +" "+"is" +" " +str(area))

Calculate Interest
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number
of years
Program Console Sample 1:
Please enter principal amount: 10000
Please Enter Rate of interest in %: 0.1
Enter number of years for investment: 5
After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1
# In[ ]:


principal_amount=int(input("Please enter principal amount: "))
interest=float(input("Please Enter Rate of interest in %:"))
year=float(input("Enter number of years for investment:"))
future_value  =principal_amount *((1+(0.01*interest)) ** year)
print(uture_value )




# In[ ]:





# In[ ]:




