from keygen import get_phi, get_prime_numbers, calc_cop
from text_conversion import string_to_list_of_char, char_to_ascii
import time


def encrypt(message: str, key: int):
    output = (message**key[0] % (key[1]))
    return output


def rsa_key_gen(n1: int, n2: int):
    """
  take two numbers and generate prime numbers 
  for public and private key
  """
    prime_numbers = get_prime_numbers(n1, n2)
    p = prime_numbers[0]
    q = prime_numbers[1]
    n = p * q
    phi = get_phi(p, q)
    e = calc_cop(phi)
    d = pow(e, -1, int(phi))
    public = [e, n]
    private = [d, n]
    return public, private


def encrypt_message(user_input: str, n1: int, n2: int):
    time_start = time.time()
    public_key, private_key = rsa_key_gen(n1, n2)
    print("\nThis is private key: ", private_key)
    print("This is public key: ", public_key)
    message = user_input
    message_char = message_char = string_to_list_of_char(message)
    message_char_int = char_to_ascii(message_char)
    encrypt_list = []
    for tmp in message_char_int:
        encrypted_message = encrypt(tmp, private_key)
        encrypt_list.append(encrypted_message)
    recovered_list = []
    for i in encrypt_list:
        recovered_tmp = encrypt(i, public_key)
        recovered_list.append(recovered_tmp)
    recovered_char = char_to_ascii(recovered_list)
    recovered_message = string_to_list_of_char(recovered_char)
    print("This is the message before encryption: ", message)
    print("This is the message in a character list: ", message_char)
    print("This is the message in ACSII format: ", message_char_int)
    print("This is the encrypted list: ", encrypt_list)
    print("This is the recovered list in ASCII format: ", recovered_list)
    print("This is the recovered message character list", recovered_char)
    print("This is the recovered message: ", recovered_message)
    time_dur = (time.time() - time_start)
    print("\nThis is the time it took: ", time_dur, " for integers: ", n1,
          " and ", n2)


(encrypt_message("hello", 1, 100001))
