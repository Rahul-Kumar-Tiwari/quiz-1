#hangman version1

import random
import string
import time

print("")
print("")
print("			********************Welcome*********************")
print("			**************Let's Play Hangman****************")
print("")
print("____________")
print("Instruction:")
print("------------")
print("")
print("A game for two in which one player tries to guess the letters of a word,\nthe other player recording failed attempts by drawing a gallows and someone hanging on it,\nline by line")
print("			------------------------------------------------------------")
print("					you got maximum 9 guesses")
print("			============================================================")
print(".-----")
time.sleep(1)
print("|    |")
time.sleep(1)
print("|    O")
time.sleep(1)
print("|    |")
time.sleep(1)
print("|  ~~.~~")
time.sleep(1)
print("|    |")
time.sleep(1)
print("|   / \ ")
time.sleep(1)
print("Let's Start")
print("")
animal=["panda","tiger","lion","giraffe","cat","hippo","pyhton","leopard","chameleon","camel","Chimpanzee","buffalo","butterfly"]
cricplayer=["virat","kohli","dhoni","pollard","rahul","sachin","yuvraj","sahwag","hardik","rohit","gayle","warner"]
color=["red","pink","white","yellow","black","green","voilet","maroon","purple","navy","teal","beige","orange","coral"]
car=["Nissan","Toyota"," Honda","Chevrolet","Mercedes","Volvo","Cadillac","Lexus","audi"]

print("1.Animal")
time.sleep(1)
print("2.cricplayer")
time.sleep(1)
print("3.color")
time.sleep(1)
print("4.car")
time.sleep(1)
print("5.Exit")
time.sleep(1)
choice=int(input("Enter your choice:"))

def animal_f():
	lista=[]
	animal_v=random.choice(animal).lower()
	n=len(animal_v)
	
	for x in animal_v:
		lista.append(x)
	#print(" ".join(lista))
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")
		search=search.lower()
		
		if search in lista:
			index=lista.index(search)
			lista[index]="*"
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")
		
def cricplayer_f():
	lista=[]
	cric_v=random.choice(cricplayer).lower()
	n=len(cric_v)
	
	for x in cric_v:
		lista.append(x)
	#print(" ".join(lista))
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")
		search=search.lower()
		
		if search in lista:
			index=lista.index(search)
			lista[index]="*"
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")
		
def color_f():
	lista=[]
	color_v=random.choice(color).lower()
	n=len(color_v)
	
	for x in color_v:
		lista.append(x)
	#print(" ".join(lista))
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")
		search=search.lower()
		
		if search in lista:
			index=lista.index(search)
			lista[index]="*"
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")

		
		
def car_f():
	lista=[]
	car_v=random.choice(car).lower()
	n=len(car_v)
	
	for x in car_v:
		lista.append(x)
	#print(" ".join(lista))
	
	list=[]
	for x in range(n):
		list.append("_")
	print(" ".join(list))
	
	count=0
	sucess=0
	while count<9 and sucess<n:		
		search=input("enter your guess...")
		search=search.lower()
		
		if search in lista:
			index=lista.index(search)
			lista[index]="*"
			list[index]=search
			print(" ".join(list))
			print("")
			sucess+=1			
		else:
			print(" ".join(list))
			count+=1
			print((9-count),"chances remainig")
			print(" ")
				
	if count<9 and sucess==n:
		print(" ")
		print("Congrats ,you won!")
	else:
		print("")
		print("you loose..try again later")
			
def exit_f():
	exit()
		
if choice==1:
	animal_f()
elif choice==2:
	cricplayer_f()
elif choice==3:
	color_f()
elif choice==4:
	car_f()
else: 
	exit_f()
	

	

