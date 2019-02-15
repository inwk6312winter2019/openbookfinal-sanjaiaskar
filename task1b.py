import string

#fi=open('Book1.txt')
#file1=fi.read()

def print_book(books):
	count=0
	mydict=dict()
	com_dict=dict()
	for line in books.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
#		print(myword)
		count=count+1
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1

	print('The total no of words in the Book is:',count)
	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))
	mylist.sort(reverse=True)
	print("the most common 20 words in Book are:")
	for freq,word in mylist[:20]:
		print(word,freq,sep='\t')
	for char in mylist[:20]:
		com_dict[char]=com_dict.get(char,0)+1
	print("\nDictionery containing the most common 20 words:\n")
	print(com_dict)

fi1=open('Book1.txt')
file1=fi1.read()
fi2=open('Book2.txt')
file2=fi2.read()
fi3=open('Book3.txt')
file3=fi3.read()
print("=============Book1 Data=============")
print_book(file1)
print("=============Book2 Data=============")
print_book(file2)
print("=============Book3 Data=============")
print_book(file3)
