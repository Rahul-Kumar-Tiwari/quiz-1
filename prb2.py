#quiz
print("<----Hello! Let's get started---->")
print("|********************************|")
print("We Welcome you to Our Introdution Application....")
print("|********************************|")
print("Featuring the Basic Project for introduction..")
print("|********************************|")
print("Design By MALAY KUMAR")
print("|********************************|")
print("<----:Please Enter Your gender:---->")
gender=input("If You are Male Plz Write 'M or m' and 'F or f' for Female:")

def nam():	#this function is called when user enter the name orher than in alphabet
	name=input("What Is Your Good Name : ")
	if name.isalpha():	#if name is only in alphabet then if execute
		print("Hii Sir, Your Name is",name)
		print("")
		print("I Would like to collect some more information About You")
		age=input("Enter your age (Eligibility criteria is more than 20):")
		if age.isdigit():	#if age is only in digit then this condition execute
			if int(age)>20:		#if age is greater than 20 then this condition execute
				print("Welcome",name,"sir,as your age is",age,"years,You are eligible for Python Fundamental Course...")
			else:
				print("Sir!..you are not eligible for Python Fundamental course...")
		else:
			print("Sir!..please enter your age correctly(in digit)..")
			ag()	#this function is called when user enter the age other than iinteger
	else:	#if the user enter the name other than in alphabet then this condition execute
		print("Sir!..please enter your name correctly(in alphabet)..")
		nam()	#this function is called when user enter the name orher than in alphabet
				
def ag(): #this function is called when user enter the age other than integer
	age=input("Enter your age (Eligibility criteria is more than 20):")
	if age.isdigit():	#if age is only in digit then this condition execute
		if int(age)>20:	#if age is greater than 20 then this condition execute
			print("Welcome",name,"sir,as your age is",age,"years,You are eligible for Python Fundamental Course...")
		else:
			print("Sir!..you are not eligible for Python Fundamental course...")
	else:	#if user enter the age other than integer
		print("Sir!..please enter your age correctly(in digit)..")
		ag()	#this function is called when user enter the age other than integer
		
def namf():	#this function is called when user enter the name orher than in alphabet
	name=input("What Is Your Good Name : ")
	if name.isalpha():	#if name is only in alphabet then if execute
		print("Hii Mam, Your Name is",name)
		print("I Would like to collect some more information About You")
		age=input("Enter your age (Eligibility criteria is more than 19):")
		if age.isdigit():	#if age is only in digit then this condition execute
			if int(age)>19:	#if age is greater than 19 then this condition execute
				print("Welcome",name,"Mam,as your age is",age,"years,You are eligible for core Java Fundamental course..")
			else:
				print("Sorry!..you are not eligible for core Java Fundamental course")
		else:
			print("Mam!..please enter your age correctly(in digit)")
			agf()	#this function is called when user enter the age other than integer
	else:	#if the user enter the name other than in alphabet then this condition execute
		print("Mam!..please enter your name correctly(in alphabet)..")
		namf()	#this function is called when user enter the name orher than in alphabet
		
def agf():#this function is called when user enter the age other than integer
	age=input("Enter your age (Eligibility criteria is more than 19):")
	if age.isdigit():	#if age is only in digit then this condition execute
		if int(age)>19:		#if age is greater than 19 then this condition execute
			print("Welcome",name,"Mam,as your age is",age,"years,You are eligible for core Java Fundamental course..")
		else:
			print("Sorry!..you are not eligible for core Java Fundamental course")
	else:	#if user enter the age other than integer
		print("Mam!..please enter your age correctly(in digit)")
		agf()	#this function is called when user enter the age other than integer

def el():	#if user enter gender other than in m/M or f/F
	print("please enter your age correctly...!!")
	gender=input("If You are Male Plz Write 'M or m' and 'F or f' for Female:")
	if gender=="m" or gender=="M":
		namb()	#
	elif gender=="f" or gender=="F":
		namfg()
	else:
		el()

def namb():	#this function is called if user enter name other than integer in final else condition
	print("Hello Sir,,We Welcome you on Board...")
	name=input("What Is Your Good Name : ")
	if name.isalpha():
		print("Hii Sir, Your Name is",name)
		print("")
		print("I Would like to collect some more information About You")
		age=input("Enter your age (Eligibility criteria is more than 20):")
		if age.isdigit():
			if int(age)>20:
				print("Welcome",name,"sir,as your age is",age,"years,You are eligible for Python Fundamental Course...")
			else:
				print("Sir!..you are not eligible for Python Fundamental course...")
		else:
			print("Sir!..please enter your age correctly(in digit)..")
			ag()
	else:
		print("Sir!..please enter your name correctly(in alphabet)..")
		nam()

def namfg():	#this function is called if user enter name other than integer in final else condition
	print("Hello Mam,,We Welcome you on board...")
	name=input("What Is Your Good Name : ")
	if name.isalpha():
		print("Hii Mam, Your Name is",name)
		print("I Would like to collect some more information About You")
		age=input("Enter your age (Eligibility criteria is more than 19):")
		if age.isdigit():
			if int(age)>19:
				print("Welcome",name,"Mam,as your age is",age,"years,You are eligible for core Java Fundamental course..")
			else:
				print("Sorry!..you are not eligible for core Java Fundamental course")
		else:
			print("Mam!..please enter your age correctly(in digit)")
			agf()
	else:
		print("Mam!..please enter your name correctly(in alphabet)..")
		namf()

if gender=="m" or gender=="M":
	print("Hello Sir,,We Welcome you on Board...")
	name=input("What Is Your Good Name : ")
	
	if name.isalpha():
		print("Hii Sir, Your Name is",name)
		print("")
		print("I Would like to collect some more information About You")
		age=input("Enter your age (Eligibility criteria is more than 20):")
		if age.isdigit():
			if int(age)>20:
				print("Welcome",name,"sir,as your age is",age,"years,You are eligible for Python Fundamental Course...")
			else:
				print("Sir!..you are not eligible for Python Fundamental course...")
		else:
			print("Sir!..please enter your age correctly(in digit)..")
			ag()
	else:
		print("Sir!..please enter your name correctly(in alphabet)..")
		nam()
				
elif gender=="f" or gender=="F":
	print("Hello Mam,,We Welcome you on Board...")
	name=input("What Is Your Good Name : ")
	
	if name.isalpha():
		print("Hii Mam, Your Name is",name)
		print("I Would like to collect some more information About You")
		age=input("Enter your age (Eligibility criteria is more than 19):")
		if age.isdigit():
			if int(age)>19:
				print("Welcome",name,"Mam,as your age is",age,"years,You are eligible for core Java Fundamental course..")
			else:
				print("Sorry!..you are not eligible for core Java Fundamental course")
		else:
			print("Mam!..please enter your age correctly(in digit)")
			agf()
	else:
		print("Mam!..please enter your name correctly(in alphabet)..")
		namf()
				
else:
	print("please enter your gender correctly...!!")
	gender=input("If You are Male Plz Write 'M or m' and 'F or f' for Female:")
	if gender=="m" or gender=="M":
		namb()
	elif gender=="f" or gender=="F":
		namfg()
	else:
		el()
		
		
		