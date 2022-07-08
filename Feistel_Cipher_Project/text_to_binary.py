import numpy as np
def ascii_to_binary(user_input:list):
  """
  this function instantiate a new list called output
  then checks if the type is a list for the user_input
  next it create it use one fo the input, input_type and check if the values are binary or not
  next it checks the list if all character in said input are all ints if not the function would stop
  if binary = true then we convert to a string so we can reconvert it from binary value which is base two to a base 10 int 
  if binary = false then we use the format function to format the value to binary

  """
  output_list = []
  #check if the input is an integer, and that it is small enough to be represented as 8 bit binary
  if isinstance(user_input[0], int) and user_input[0] < 500:
    for item in user_input:
      output_list.append(np.binary_repr(item,width=8)) 
  #check if the input is of type string
  elif isinstance(user_input[0], str):
    for item in user_input:
      output_list.append(int(str(item),2)) 
  #print an error message if the input type is incorrect
  else:
    print('the input type is incorrect')
  return output_list


def string_to_ascii(user_input):
  """
  this function instantiate a new list
  then checks if the type is a list first
  next it checks the list if all character in said input are the same type using the any() function
  and use and if then clause to convert based on the type input
  finally it loops through based on type and appends and converts using ord to go to string
  and chr to go from ascii to string
  """
  newList = []
  if type(user_input) is list:
    if all(type(char)is str for char in user_input):
       for char in user_input:
         newList.append(ord(char))
    elif all(type(char) is int for char in user_input):
      for char in user_input:
        newList.append(chr(char))
  return newList

# Test inputs for professor
#print(string_to_ascii(['h','e','l','l','o',' ','w','o','r','l','d']))
#print(string_to_ascii([104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]))

def string_to_list_or_vice_versa(user_input):
  '''
  take a userinput of anytype and if is a string use list function to turn it into a list,
  if it is a list use the join function on an empty string to make concencate it all
  '''
  if type(user_input) is str:
    newlist = list(user_input)
    return (newlist)
  if type(user_input) is list:
    newString = ''.join(user_input)
    return (newString)

#string_to_list_or_vice_versa("hello")
#string_to_list_or_vice_versa(['h','e','l', 'l', 'o'])
