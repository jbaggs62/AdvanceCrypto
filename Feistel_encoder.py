import numpy as np
#encryption and decryption round
def enc_dec_round(input_string, key):
#split the L0 and R0
  L_0 = input_string[:4]
  R_0 = input_string[4:]
  #convert binary string to integer and compute the feistel function
  key_int = int(key,2)
  L_0_int = int(L_0,2)
  R_0_int = int(R_0,2)
  function_output_int = 2*(R_0_int**key_int)%(2**4)
  #function_output_binary = bin(function_output)[2:]
  #xor the L0 and the output of the feistel function
  xor_result_int = L_0_int^function_output_int
  xor_result_binary = np.binary_repr(xor_result_int,width=4)
  #output L1 and R1
  L_1 = R_0
  R_1 = xor_result_binary
  output_bin_string = L_1+R_1
  return output_bin_string