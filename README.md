# RSA-Algorithm-Implementation
A program which implements the RSA Algorithm to encrypt and decrypt a message.

The RSA algorithm is the basis of a cryptosystem - a suite of cryptographic algorithms that are used for specific security services or purposes - which enables public key encryption and is widely used to secure sensitive data, particularly when it is being sent over an insecure network such as the internet.

This program prompts the user to input the values of two large, distinct primes (p and q), the plaintext integer and an arbitrary integer e from a list of possible e’s allowed (gcd(e, (p−1)(q−1)) = 1 and 1 < e < (p−1)(q−1). 

The program calculates the public key, the private key, the encrypted message and the decrypted message.

Warning: The program only works for plaintext  whose integer representation is less than n.
