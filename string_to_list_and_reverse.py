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
