import sympy

def euler_phi(n):
    if sympy.isprime(n):
        return n - 1
    else:
        factors = sympy.factorint(n)
        result = 1
        for prime, exp in factors.items():
            result *= (prime - 1) * prime ** (exp - 1)
        return result

p = 5729349851584029373
q = 8064115072964340661

n = p * q # Thay đổi giá trị của n theo nhu cầu của bạn
phi_n = euler_phi(n)
print(f"Phi(n) = {phi_n}")
