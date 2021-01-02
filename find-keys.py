from math import gcd

# RSA Implementation (step-by-step)

# Setting up RSA
# randomly choose two large, distinct primes p and q
p = int(input('Choose a large prime number p = '))
q = int(input('Choose another large prime number q = '))
n = p * q

# Select an arbitrary integer e so that gcd(e, (p−1)(q−1)) = 1 and 1 < e < (p−1)(q−1)
phi = (p - 1) * (q - 1)
possible_e = []


def find_e(x):
    for y in range(2, x):
        if gcd(y, x) == 1:
            possible_e.append(y)
    return possible_e


e = int(input('Choose a value for e from the following list:\n' + str((find_e(phi))) + '\ne = '))


# Solve the congruence
# ed≡1 (mod(p−1)(q−1)) for an integer d where 1 < d < (p − 1)(q − 1)

# e_gcd and mod_inv taken from
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Modular_inverse

# return (g, x, y) such that a*x + b*y = g = gcd(a, b)
def e_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = e_gcd(b_mod_a, a)
        return g, y - b_div_a * x, x


# return x such that (x * a) % b == 1
def mod_inv(a, b):
    g, x, _ = e_gcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b


d = (mod_inv(int(e), phi))


print('Results:')
print('Public Key: (' + str(e) + ',' + str(n) + ')')
print('Private Key: (' + str(e) + ',' + str(d) + ')')
