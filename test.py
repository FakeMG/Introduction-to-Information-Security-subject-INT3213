import random

def modular_exponentiation(a, b, m):
    result = 1  # Khởi tạo giá trị kết quả ban đầu là 1
    a = a % m  # Tối giản a theo modulo m

    while b > 0:
        # Nếu b lẻ, nhân kết quả với a và lấy modulo m
        if b % 2 == 1:
            result = (result * a) % m
        
        # Bình phương a và lấy modulo m
        a = (a * a) % m

        # Chia b cho 2
        b //= 2

    return result

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return m + 1
    else:
        return x % m

p = 5933
q = 5441

n = p * q

k = 3

s1 = 157
s2 = 43215
s3 = 4646

b1 = 1
b2 = 0
b3 = 1

v1 = (-1 ** b1) * mod_inverse(s1**2, n)
v1 = v1 % n
v2 = (-1 ** b2) * mod_inverse(s2**2, n)
v2 = v2 % n
v3 = (-1 ** b3) * mod_inverse(s3**2, n)
v3 = v3 % n

r = 1279
    
b_r = 1

x = pow(-1,b_r) * r**2 % n

y = r * s3 % n

z = y**2 * v3 % n

print(f"p:{p}")
print(f"q:{q}")
print(f"n:{n}")
print(f"v1:{v1}")
print(f"v2:{v2}")
print(f"v3:{v3}")
print(f"x:{x}")
print(f"y:{y}")
print(f"z:{z}")

if z == x or z == x * (-1):
    print("True")
else:
    print("False")