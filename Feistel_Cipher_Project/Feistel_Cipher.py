import numpy as np
from Feistel_encoder import enc_dec_round
from text_to_binary import string_to_list_or_vice_versa, string_to_ascii, ascii_to_binary

#main feistel cipher function
def feistel_cipher(input:str, keys:list):
  """
  This function takes an input of the type string, and a list of encryption keys
  It then converts the keys to binary from integer
  Next it convert the input to binary
  After everything is in binary a loop goes through and encrypts each binary char n times where n = the number of keys
  it takes the back for and the front four digits of the binary and swaps them and appends them to a new list 
  """
  #initialize the key value and convert the key to 4 dig binary
  int_keys = keys
  binary_keys = []
  for key in int_keys:
    binary_keys.append(np.binary_repr(key,width=4))
  #convert message string to 8 bit binary
  input_char = string_to_list_or_vice_versa(input)
  input_int = string_to_ascii(input_char)
  input_binary = ascii_to_binary(input_int)
  #encryption round
  encrypted_char_bin = []
  for char in input_binary:
    temp_char = char
    for key in binary_keys:
      temp_char = enc_dec_round(temp_char,key)
    temp_char_swap = temp_char[4:]+temp_char[:4]
    encrypted_char_bin.append(temp_char_swap)
  #convert 8 bit binary cipher to string
  enc_char_int = ascii_to_binary(encrypted_char_bin)
  enc_char_list = string_to_ascii(enc_char_int)
  enc_string = string_to_list_or_vice_versa(enc_char_list)
  return enc_string
#test 1
test_1_keys = [0,1,5,6,7,8]
test_1_keys_keys_reverse = np.flip(test_1_keys)
message_1 = 'hello world'
cipher_1 = feistel_cipher(message_1, test_1_keys)
recovered_message_1 = feistel_cipher(cipher_1, test_1_keys_keys_reverse)
print(f'\ntest 1: ')
print(f'encryption keys: {test_1_keys}')
print(f'original message: {message_1}')
print(f'ecnrypted_message: {cipher_1}')
print(f'recovered message: {recovered_message_1}')


#test 2
test_1_keys = [0,3,7,8,9,15]
test_1_keys_keys_reverse = np.flip(test_1_keys)
message_1 = 'testing out this cool cipher'
cipher_1 = feistel_cipher(message_1, test_1_keys)
recovered_message_1 = feistel_cipher(cipher_1, test_1_keys_keys_reverse)
print(f'\ntest 1: ')
print(f'encryption keys: {test_1_keys}')
print(f'original message: {message_1}')
print(f'encypted message: {cipher_1}')
print(f'recovered message: {recovered_message_1}')
