# These challenges can be spotted when given mutiple c cipher texts and multiple n moduli. e must be the same number of given c and n pairs.

from functools import reduce
from Crypto.Util.number import *
import binascii
import sympy


e = 3

bitsize = 512

n1 = n2 = n3 = 0

while ((sympy.gcd(n3, n2) != 1) and (sympy.gcd(n1, n2) != 1) and (sympy.gcd(n1, n2) != 1)):

    n1 = getPrime(bitsize)
    n2 = getPrime(bitsize)
    n3 = getPrime(bitsize)
    # n4 = getPrime( bitsize )


# print n1, n2, n3
print("n1 = ", n1)
print("n2 = ", n2)
print("n3 = ", n3)
# print "n4 = ", n4
# print sympy.gcd(n1,n2), sympy.gcd(n1,n3), sympy.gcd(n3,n2)

m = 'USCGA{the_chinese_remainder_theorem_is_so_cool}'
m = binascii.hexlify(m)
m = int(m, 16)

c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
c3 = pow(m, e, n3)
# c4 = pow(m, e, n4)
print("")

print("c1 = ", c1)
print("c2 = ", c2)
print("c3 = ", c3)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        print("n_i", n_i)
        print("a_i", a_i)
        print("p", p)
        # sum += a_i * mul_inv(p, n_i) * p
        sum += a_i * inverse(p, n_i) * p
        print("sum", sum)
    return sum % prod


x = chinese_remainder([n1, n2, n3], [c1, c2, c3])
# print x

# 1. Simple attack
# m = sympy.root(x, e)

m = pow(sympy.E,  sympy.ln(x) / e)


print("Trey's one sum", c1 * n2 * n3 * inverse(n2*n3, n1))
# # THIS IS THE CHINESE REMAINDER THEOREM IN ONE EQUATION ... FROM TREY
# m = ( c1 * n2 * n3 * inverse( n2*n3, n1 ) + c2 * n1 * n3 * inverse( n1*n3, n2 ) + c3 * n1 * n2 * inverse( n1*n2, n3 ) ) % ( n1 * n2 * n3 )
# print m == x

# print pow(10, sympy.ln(pow(m,e)))


print("")

# print

try:
    print(hex(int(m))[2:-1].decode('hex'))
except:
    print("Supposedly odd length string...")
    print(str("0" + hex(int(m))[2:-1]).decode('hex'))
