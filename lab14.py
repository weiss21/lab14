#Lab 14


#Problem 1
def greenEggsHam():
  
  #Opens Green Eggs and Ham File. Reads it into text form. Then closes file.
  file = open("C:\Users\Weiss\Documents\GitHub\lab14\eggs.txt","rt")
  fileText = file.read()
  file.close()
  
  #create an array of words. No Spaces or dashes
  fileText = fileText.lower().replace("-", " ").split()
  
  #How many distinct Words.
  #When this is done. Delete Return, and this comment.
  unique = set(fileText)
  return len(unique)
