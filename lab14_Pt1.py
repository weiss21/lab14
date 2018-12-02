#Lab 14, Wais Robleh
#Using JES

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
    word_freq.append((k,v))
  
  #Sort from highest to lowest
  #To sort number in second array. Use
  word_freq.sort(reverse = True, key = lambda x: x[1])
  
  #Print out the total distinct count. And count for each distinct. Step 3
  print("There is a total of %s distinct words in Green Eggs and Ham" %len(unique))
  print("How often each word apears is as follows: " + "\n")
  print word_freq

  #Print out Most commonly used Word. Step 4
  print("\nThe most commonly used word is: ")
  print word_freq[0][0], " with ",word_freq[0][1]