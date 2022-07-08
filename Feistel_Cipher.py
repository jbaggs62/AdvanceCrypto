import numpy as np
from Feistel_encoder import enc_dec_round
from text_to_binary import func_0, func_1, func_2
from List_of_Charcter_to_ascii import string_to_ascii
from ascii_to_binary import ascii_to_binary
from  string_to_list_and_reverse import string_to_list_or_vice_versa



#main feistel cipher function
def feistel_cipher(message, key):
  #initialize the key value and convert the key to 4 dig binary
  all_key_int = key
  all_key_bin = []
  for i in all_key_int:
    all_key_bin.append(np.binary_repr(i,width=4))
  #convert message string to 8 bit binary
  message_char = func_0(message)
  message_char_int = func_1(message_char)
  message_char_bin = func_2(message_char_int)
  #encryption round
  cipher_char_bin = []
  for i in message_char_bin:
    temp_cipher_char = i
    for j in all_key_bin:
        temp_cipher_char = enc_dec_round(temp_cipher_char,j)
    temp_cipher_char_swap = temp_cipher_char[4:]+temp_cipher_char[:4] 
    cipher_char_bin.append(temp_cipher_char_swap)
  #convert 8 bit binary cipher to string
  cipher_char_int = func_2(cipher_char_bin)
  cipher_char = func_1(cipher_char_int)
  cipher_string = func_0(cipher_char)
  return cipher_string
#test 1
#16 keys = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
key = np.arange(16)
key_reverse = np.flip(key)
message_1 = 'hello world'
cipher_1 = feistel_cipher(message_1, key)
recovered_message_1 = feistel_cipher(cipher_1, key_reverse)
print(f'\ntest 1: ')
print(f'key: {key}')
print(f'original message: {message_1}')
print(f'cipher text: {cipher_1}')
print(f'recovered message: {recovered_message_1}')
#test 2
#16 keys = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
key = np.array([3,4,9,12,8,7])
key_reverse = np.flip(key)
message = 'this is test 2'
cipher = feistel_cipher(message, key)
recovered_message = feistel_cipher(cipher, key_reverse)
print(f'\ntest 2: ')
print(f'key: {key}')
print(f'original message: {message}')
print(f'cipher text: {cipher}')
print(f'recovered message: {recovered_message}')
#test 3
#16 keys = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
key = np.array([7,7,8,8,9,9,10,10])
key_reverse = np.flip(key)
message = 'this is the third test'
cipher = feistel_cipher(message, key)