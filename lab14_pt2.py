#Lab 14, Wais Robleh
#Using JES

#Problem 2

#Step 1. Save HTML file of website on computer completed

def head():
  
  #Step 2. Open HTML File
  file = open("/C:/Users/Weiss/Documents/GitHub/lab14/foot.html", "rt")
  
  original = file.read() 
  file.close()
  

  #Step 2. Use string processing to extract headline from paper.
  
  print len(original)
