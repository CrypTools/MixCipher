import random as rd

def encrypt(message):
  """ encrypt("123456789")
=> ('312587946', '201476835')
  """
  randomlist = [n for n in range(0, len(message))]
  rd.shuffle(randomlist)
  
  mylist = []
  
  for character in message:
     mylist.append(character)

  output = ""
  key = ""
  
  for i in range(0, len(mylist)):
    output += mylist[randomlist[i]]
    
  for element in randomlist:
    key += str(element)
  
  return output, key
