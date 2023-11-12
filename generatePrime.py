import random
import sympy

# Tạo số nguyên tố ngẫu nhiên
while True:
    p = random.randint(10**540, 10**551 - 1)
    if sympy.isprime(p):
        break

while True:
    q = random.randint(10**54, 10**55 - 1)
    if sympy.isprime(q) and q != p:
        break

print("p =", p)
print("q =", q)
