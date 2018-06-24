#calculation

print("_____welcome_____")
print("choose numbers below to perform various operation")
print("")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Raise to power")
print("5. Division")
print("6. Floor Division")
print("7. Factorail")
def again():	#here function is used to perform calculation according to user and to be used after one opeartion
	num=int(input("Enter your choice:"))
	print("")
	if type(num)==int:	#condition check-entered number is integer 
		if num==1:
			print("you want to perform addition")
			num1=int(input("enter the number:"))
			num2=int(input("enter the second one:"))
			add=num1+num2
			print("addition of two number is ",add)
			print("")
			again1()	#if user want to continue 
		
		elif num==2:
			print("you want to perform subtraction")
			num1=int(input("enter the number:"))
			num2=int(input("enter the second one:"))
			sub=num1-num2
			print("subtraction of two numbers is ",sub)
			print("")
			again1()	#if user want to continue 
		
		elif num==3:
			print("you want to perform multiplication")
			num1=int(input("enter the number:"))
			num2=int(input("enter the second one:"))
			mul=num1*num2
			print("multiplication of two number is ",mul)
			print("")
			again1()	#if user want to continue 
				
		elif num==4:
			print("you want to find power")
			num1=int(input("enter the base value:"))
			num2=int(input("enter the index value:"))
			pow=num1**num2
			print("power: ",pow)
			print("")	#if user want to continue 
			again1()
		
		elif num==5:
			print("you want to perform division")
			num1=int(input("enter the number:"))
			num2=int(input("enter the second one:"))
			div=num1/num2
			print("Division of number is",div)
			print("")
			again1()	#if user want to continue 
			
		elif num==6:
			print("you want to floor value")
			num1=int(input("enter the number:"))
			num2=int(input("enter the second one:"))
			flrdiv=num1//num2
			print("result of floor division is ",flrdiv)
			print("")
			again1()	#if user want to continue 
			
		elif num==7:
			print("you want to find factorail:")
			num=int(input("enter any number:"))
			fact=1
			for x in range(1,num+1):
				fact=fact*x
			print("factorial of that number is ",fact)
			print("")
			again1()	#if user want to continue 
			
		else:
			print("enter valid number")
			print("")
			again()		#this function called if user enter invalid number 
			
	else:	#enter number other than integer
		print("enter valid number")
		print("")
		again()		#this function called to get valid input from user 
		
def again1():	#funtion ask user taht they want to perform operation
	print("do you want to perform again or to exit press any key ")
	choice=input("enter 'y' to continue:")
	if choice=="y":
		again()		#if user want to continue after a operation
		
again()	#start the execution