#Lab 14

#Problem 1
def greenEggsHam():
  
  #Opens Green Eggs and Ham File. Reads it into text form. Then closes file.
  file = open("C:\Users\Weiss\Documents\GitHub\lab14\eggs.txt","rt")
  original = file.read()
  file.close()
  
  #create an array of words. No Spaces or dashes
  fileText = original.lower().replace("-", " ").split()
  
  #How many distinct Words. Step 1
  #When this is done. Delete Return, and this comment.
  unique = set(fileText)
  
  #Create a count of how often each of the words appears. Step 2 
  #use a dictionary
  
  wordsAppear = {}
  for i in fileText:
    wordsAppear[i] = wordsAppear.get(i, 0) + 1

  #reverse the values to be sort.
  word_freq = []
  for k, v in wordsAppear.items():
    word_freq.append((v,k))
  
  #Sort from highest to lowest
  
  word_freq.sort(reverse = True)
  return word_freq
