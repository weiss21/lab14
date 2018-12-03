#Lab 14, Wais Robleh
#Using JES

#Problem 2

#Step 1. Save HTML file of website on computer completed

#Extra Function

def head():
  
  #Step 2. Open HTML File
  file = open("/C:/Users/Weiss/Documents/GitHub/lab14/foothill.html", "r")
  fileText = file.read() 
  file.close()

  #Step 2. Use string processing to extract headline from paper.
  #place Headlines in Array
  headlines = [] 

  #a = "<h3>"
  #b = "</h3>"
  a ="&lt;h3&gt;</span>"
  b ="<span class=\"html-tag\">&lt;/h3&gt;</span>"
  
  index = 0 
  start = 0
  finish = len(fileText)
  
  while index != -1:
    index = fileText.find(a, start, finish)
    if index != -1:
      index += len(a)
    midIndex = fileText.find(b, index, finish)
    headlines.append(fileText[index:midIndex])
    start = midIndex
    
  for i in headlines:
    print i
  return 0
    
  
  
  #return headlines
  
  
  
    

