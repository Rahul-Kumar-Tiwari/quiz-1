#Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
l=[]
for x in range(10):
	l.append(int(input("enter ant number:")))

print(l)	
s=set(l)	
abc=list(s)
print(abc)
	