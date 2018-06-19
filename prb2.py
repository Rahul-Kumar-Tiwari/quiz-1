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

def nam():
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
				
def ag():
	age=input("Enter your age (Eligibility criteria is more than 20):")
	if age.isdigit():
		if int(age)>20:
			print("Welcome",name,"sir,as your age is",age,"years,You are eligible for Python Fundamental Course...")
		else:
			print("Sir!..you are not eligible for Python Fundamental course...")
	else:
		print("Sir!..please enter your age correctly(in digit)..")
		ag()
		
def namf():
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
		
def agf():
	age=input("Enter your age (Eligibility criteria is more than 19):")
	if age.isdigit():
		if int(age)>19:
			print("Welcome",name,"Mam,as your age is",age,"years,You are eligible for core Java Fundamental course..")
		else:
			print("Sorry!..you are not eligible for core Java Fundamental course")
	else:
		print("Mam!..please enter your age correctly(in digit)")
		agf()

def el():
	print("please enter your age correctly...!!")
	gender=input("If You are Male Plz Write 'M or m' and 'F or f' for Female:")
	if gender=="m" or gender=="M":
		namb()
	elif gender=="f" or gender=="F":
		namfg()
	else:
		el()

def namb():	
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

def namfg():
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
		
		
		