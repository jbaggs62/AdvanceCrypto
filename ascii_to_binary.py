def ascii_to_binary(user_input, input_type):
  """
  this function instantiate a new list
  then checks if the type is a list for the user_input
  next it create it use one fo the input, input_type and check if the values are binary or not
  next it checks the list if all character in said input are all ints if not the function would stop
  if binary = true then we convert to a string so we can reconvert it from binary value which is base two to a base 10 int 
  if binary = false then we use the format function to format the value to binary

  """
  newList = []
  if type(user_input) is list:
    if (input_type == 'binary'):
      binary = True
    elif (input_type == 'nonbinary'):
      binary = False
    if all(type(char) is int for char in user_input):
      if binary == True:
        for char in user_input:
          newChar = str(char)
          newList.append(int(newChar, 2))
      elif binary == False:
        for char in user_input:
          bValue = format(char, 'b') 
          newList.append(bValue)
      return newList
# Test inputs
#print(ascii_to_binary([1101000, 1100101, 1101100, 1101100, 1101111, 100000, 1110111, 1101111,
#1110010, 1101100, 1100100], 'binary'))
#print(ascii_to_binary([104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100], 'nonbinary'))

