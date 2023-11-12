import sympy
import math


def euler_phi(n):
    if sympy.isprime(n):
        return n - 1
    else:
        factors = sympy.factorint(n)
        result = 1
        for prime, exp in factors.items():
            result *= (prime - 1) * prime ** (exp - 1)
        return result


# Thuật toán tìm dãy các số nguyên tố cùng nhau với n mà <= n
def prime_numbers_coprime_to_n(n):
    phi_n = euler_phi(n)
    primes = [i for i in range(1, n) if math.gcd(i, n) == 1]
    return primes

print(prime_numbers_coprime_to_n(4942901016))