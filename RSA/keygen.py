import numpy as np

def get_prime_numbers(num1,num2):
  """
  function takes two know and find two prime # in the range between the two numbers
  n1 >>> n2
  """
  # get two prime #
  rov = []
  for x in range(num1,num2):
    prime = True
    for number in range(2,x):
      if x % number == 0:
        prime = False
    if prime:
      rov.append(number)
  prime_numbers = np.random.choice(rov, size = 2, replace = False)  
  prime_numbers.sort()
  return prime_numbers


def get_phi(prime_1:int,prime_2:int):
  #get phi 
  p = prime_1
  q = prime_2
  phi_value = (p-1)*(q-1)
  return phi_value

def calc_gcd(prime1,prime2):
  p = prime1
  q = prime2
  while q != 0:
    p,q = q, p%q
  return p  


def calc_cop(phi:int):
  for number in range(phi-3,2,-1):
    if calc_gcd(phi, number) == 1:
      return number
  return -1 

def multi_inverse(e:int, n:int):
  output = -2
  for item in range(1,n):
    if ((e%n)*(item%n) % n ==1):
      output = item
    return output

