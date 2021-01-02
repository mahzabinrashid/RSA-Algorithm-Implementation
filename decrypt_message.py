# RSA Encryption: To decrypt a message

# input the private key
d = int(input('Input d (first number of the private key) = '))
n = int(input('Input n (second number of the private key) = '))
ciphertext = int(input('Ciphertext = '))

r = pow(ciphertext, d, n)

# RSA Encryption
if r > n:
    print("You can only decrypt messages whose integer representation is less than n.")
else:
    print('Decrypted message = ' + str(r))
