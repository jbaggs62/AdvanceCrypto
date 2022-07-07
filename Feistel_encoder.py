import numpy as np

#encryption and decryption round
def encoder_function(input:str, key):
#split the L0 and R0
  Left_0 = input[:4]
  Right_0 = input[4:]
  #convert to int from binary
  Right_0 = int(Right_0,2)
  key = int(key,2)
  Left_0 = int(Left_0,2)
  feistel_encryption_output= 2*(Right_0**key) %(2**4)
  #xor 
  xor_int= Left_0 ^ feistel_encryption_output
  xor_binary = np.binary_repr(xor_int,width=4)
  #output L1 and R1
  Right_0 = str(Right_0)
  L_1 = Right_0
  R_1 = xor_binary
  output = L_1+R_1
  return output
