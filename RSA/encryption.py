from keygen import get_phi, get_prime_numbers, calc_cop, multi_inverse

def encrypt(message, key):
  output = (message**key[0]%(key[1]))
  return output


def rsa_key_gen(n1,n2):
  prime_numbers = get_prime_numbers(n1,n2)
  p = prime_numbers[0]
  q = prime_numbers[1]
  n = p*q
  phi = get_phi(p,q)
  e = calc_cop(phi)
  d = multi_inverse(e,phi)
  public = [e,n]
  private = [d,n]
  return public, private

n1 = 7
n2 = 1000
public_key, private_key = rsa_key_gen(n1,n2)
message = 20
encrypted_message = encrypt(message,private_key)
recovered_message = encrypt(encrypted_message,public_key)
print(message)
print(encrypted_message)
print(recovered_message)
