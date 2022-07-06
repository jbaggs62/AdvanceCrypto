def encoder_function(input, key):
  ## split binary numbers
  middle_point = int(len(input)//2)
  Left_0 = input[0:middle_point]
  Right_0 = input[middle_point::]
  ## convert to int
  Left_0 = int(Left_0)
  Right_0 = int(Right_0)
  key = int(key)
  Left_1 = Right_0
  Right_1 = feistel_function(Left_0, Right_0, key)
  Left_1 = str(Left_1)
  Right_1 = str(Right_1)
  Output = Left_1 + Right_1
  return Output
  
  
  
  
def feistel_function(Left_0,Right_0,key):
  feistel_result = (2*(Right_0**key))%(2**4)
  output = format(feistel_result, '04b')
  output = int(output)
  Right_1 = Left_0 ^ output
  return Right_1



#input = 200
#input = format(input,'08b')
#Key = 5
#Key = format(Key,'04b') 
