

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