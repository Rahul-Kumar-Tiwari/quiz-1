# create a program that asks the user to enter their name and age . print out a message addressed to them that tell them that \
#they turn 100 years.

name=input("enter your name:")
age=int(input("enter your age:"))
if age>101:
	print(name,",congrats! you turned 100")
else:
	print(name,",you don't turned 100")
	
 
#WAP to print a number divisible by 7 not 5

for x in range(2000,3201):#3200 included
	if x%7==0:
		if x%5==0:
			pass #if number divisible by then pass
		else:
			print(x)
		
#WAP which accepts a sequence if comma separated variable and generate a list

abc=input("enter number separated by ,: ")
l=abc.split(",")#split number seaprated by , and return list
print(l)
print(tuple(l))

#WAP that accepts a sentence and calculate the upper and lower case letter

abc=input("Enter any sentence: ")
a=0
b=0

for x in abc:
	if x.isupper():
		a+=1
	elif x.islower():
		b+=1
	elif x.isspace():
		pass
print("total uppercase letter",a)
print("total lowercase letter",b)
 