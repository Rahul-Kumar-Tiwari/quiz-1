#to find entered number is keyword or not

#method-1

def keywords():
	d={1:'false',2:"none",3:"true",4:"and",5:"as",6:"assert",7:"break",8:"class",9:"continue",10:"def",11:"del",12:"elif",13:"else",14:"except",15:"finally",16:"for",17:"from",18:"global",19:"if",20:"import",21:"in",22:"is",23:"lamba",24:"nonlocal",25:"not",26:"or",27:"pass",28:"raise",29:"return",30:"try",31:"while",32:"with",33:"yield"}
	search=input("enter a keyword:")
	flag=0
	for x in range(1,34):
		if d[x]==search:
			print(search, "is a keyword")
			flag=1
			break
	
	if flag==0:
		print(search,"is not a keyword")
		print('keywords:')
		for x in range(1,34):
			print(d[x])
		
			
			
keywords()