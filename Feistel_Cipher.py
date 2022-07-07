import numpy as np
from Feistel_encoder import encoder_function
from List_of_Charcter_to_ascii import string_to_ascii
from ascii_to_binary import ascii_to_binary
from  string_to_list_and_reverse import string_to_list_or_vice_versa



user_input = "hello world"
def Feistel_cipher(user_input:str, key:list):
  # convert input to string 
  string_input = string_to_list_or_vice_versa(user_input)
  int_input = string_to_ascii(string_input)
  binary_input = ascii_to_binary(int_input, 'nonbinary')
  # create list to append encoded values in
  list_of_encoded = []
  binary_keys = []
  for keys in key:
    binary_keys.append(np.binary_repr(keys, width=4))
  # for each item in my input I want to loop through
  encrypted_char = []
  for item in binary_input:
    temp_value = item
    for key in binary_keys:
      temp_value = encoder_function(temp_value,key)
    temp_cipher_char_swap = temp_value[4:]+temp_value[:4] 
    encrypted_char.append(temp_cipher_char_swap)
  output = ascii_to_binary(list_of_encoded, 'binary')
  output = string_to_ascii(output)
  output = string_to_list_or_vice_versa(output)
  return output


#test 1
#16 keys = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
key = np.arange(16)
key_reverse = np.flip(key)
message_1 = 'hello world'
cipher_1 = Feistel_cipher(message_1, key)
recovered_message_1 = Feistel_cipher(cipher_1, key_reverse)
print(f'\ntest 1: ')
print(f'key: {key}')
print(f'original message: {message_1}')
print(f'cipher text: {cipher_1}')
print(f'recovered message: {recovered_message_1}')