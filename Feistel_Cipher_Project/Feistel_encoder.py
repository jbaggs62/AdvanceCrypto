import numpy as np
#encryption and decryption round
def enc_dec_round(input_string, key):
#split the L0 and R0
  Left_inital = input_string[:4]
  Right_inital = input_string[4:]
  #convert binary string to integer and compute the feistel function
  key_int = int(key,2)
  Left_int = int(Left_inital,2)
  Right_int = int(Right_inital,2)
  function_output_int = 2*(Right_int**key_int)%(2**4)
  #function_output_binary = bin(function_output)[2:]
  #xor the L0 and the output of the feistel function
  xor_func_result_int = Left_int^function_output_int
  xor_func_result_binary = np.binary_repr(xor_func_result_int,width=4)
  #output L1 and R1
  Left_output = Right_inital
  Right_output = xor_func_result_binary
  output_bin_string = Left_output+Right_output
  return output_bin_string
