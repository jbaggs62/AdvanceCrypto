from Feistel_encoder import encoder_function
from List_of_Charcter_to_ascii import string_to_ascii
from ascii_to_binary import ascii_to_binary
from  string_to_list_and_reverse import string_to_list_or_vice_versa


List_of_Keys = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

user_input = "hello world"
def Feistel_cipher(user_input, key):
  # convert input
  input = string_to_list_or_vice_versa(user_input)
  input = string_to_ascii(input)
  input = ascii_to_binary(input, 'nonbinary')
  # create list to append encoded values in
  list_of_encoded = []
  # for each item in my input I want to loop through
  for item in input:
    temp_value = item
    for keys in List_of_Keys:
      temp_value = encoder_function(temp_value,keys)
      print("Item is ",item," and key is ",keys,"and tmpval is ",temp_value)
  output = ascii_to_binary(list_of_encoded, 'binary')
  output = string_to_ascii(output)
  output = string_to_list_or_vice_versa(output)
  return output


print(Feistel_cipher(user_input, List_of_Keys))
