file1= open('Book1.txt','r')
file1=file1.readlines()

def unique_words(file):
  result=[]
  for line in file:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in result:
        result.append(word)
  print(result)

unique_words(file1) 

def count_the_article(file):
  count=0
  result=[]
  for line in file:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in result:
         result.append(word)
  print(len(result))

count_the_article(file1)

def sorted_words(file):
    result=[]
    for line in file:
        line=line.strip()
        line=line.split()
        for word in line:
            if word not in result:
                result.append(word)
    result.sort(key = len,reverse = True)
    print(result)

sorted_words(file1)

def character_word_count(file):
    hist=dict()
    for line in file:
        line=line.lower()
        line=line.strip()
        line=line.split()
        for word in line:
            if word not in hist:
                hist[word]=1
            else:
                hist[word]+=1
    print(hist)

character_word_count(file1)

def starts_with_vow(file):
    count=0
    result=[]
    for line in file:
        line=line.lower()
        line=line.strip()
        line=line.split()
        for word in line:
            if word not in result:
                result.append(word)
    for item in result:
        if item[0] in ("a", "e", "i", "o", "u"):
            count+=1
    print(count)

starts_with_vow(file1)

