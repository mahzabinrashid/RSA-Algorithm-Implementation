# RSA Encryption: To encrypt a message as ciphertext

# input the public key
e = int(input('Input e (first number of the public key) = '))
n = int(input('Input n (second number of the public key) = '))
plaintext = int(input('Plaintext = '))

# RSA Encryption
if plaintext > n:
    print("You can only encrypt messages whose integer representation is less than n.")
else:
    c = pow(plaintext, e, n)

print('Encrypted message = ' + str(c))
