import numpy as np

#encryption and decryption round
def encoder_function(input, key):
#split the L0 and R0
Left_0 = input_string[:4]
Right_0 = input_string[4:]
#convert to int from binary
Right_0 = int(R_0,2)
key = int(key,2)
Left_0 = int(L_0,2)
feistel_encryption_output= 2*(R_0_int**key_int) %(2**4)
#xor 
xor_int= L_0_int^function_output_int
xor_binary = np.binary_repr(xor_int,width=4)
#output L1 and R1
L_1 = R_0
R_1 = xor_binary
output = L_1+R_1
return output
