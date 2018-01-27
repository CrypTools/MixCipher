def decrypt(message, key):
  """ decrypt("312587946", "201476835")
=> '123456789'
  """
  length = len(message)
  
  initial = []
  for char in message:
    initial.append(char)
    
  outputlist = []
  for i in range(length):
    outputlist.append("")

  for i in range(length):
    outputlist[int(key[i])] = initial[i]
  
  output = ""
  for i in range(length):
    output += outputlist[i]
  
  return output
