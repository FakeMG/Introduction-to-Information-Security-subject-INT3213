from sympy import primerange
from sympy import Symbol
from sympy import solve

def count_primes_in_range(n):
    primes = list(primerange(0, n))
    return len(primes)

# Số có tầm 100 chữ số
n = 1000000

prime_count = count_primes_in_range(n)
print(f"Số lượng số nguyên tố từ 0 đến n là: {prime_count}")