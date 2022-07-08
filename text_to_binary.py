import numpy as np
#string-charater converter
def func_0(input_str):
  output = None
  #checks if the input is a string
  if isinstance(input_str, str):
    output = list(input_str) #list() convert a string to a list of character
  #checks if the input is a list
  elif isinstance(input_str, list):
    output = ''
  for i in input_str:
    output += i #combine all characters a string
  #print an error message if the input type is incorrect
  else:
    print('incorrect input type')
  return output
#character-ASCII converter
def func_1(input_list):
  output = []
  #check if the input is a list of characters
  if isinstance(input_list[0], str):
    for i in input_list:
      output.append(ord(i)) #ord() converts a character to ascii integer
  #check if the input is a list of integer
  elif isinstance(input_list[0], int):
    for i in input_list:
      output.append(chr(i)) #char() converts a ascii integer to character
  #print an error message if the input type is incorrect
  else:
    print('incorrect input type')
  return output
#ASCII-binary converter
def func_2(input_list):
  output = []
  #check if the input is an integer(ASCII)
  if isinstance(input_list[0], int) and input_list[0] < 500:
    for i in input_list:
      output.append(np.binary_repr(i,width=8)) #bin() converts an integer to a binary string, int() converts to the binary string to a binary integer
  #check if the input is an string of binary
  elif isinstance(input_list[0], str):
    for i in input_list:
      output.append(int(str(i),2)) #str() converts a binary integer to a binary string, int() converts to the binary string to a integer
  #print an error message if the input type is incorrect
  else:
    print('incorrect input type')
  return output