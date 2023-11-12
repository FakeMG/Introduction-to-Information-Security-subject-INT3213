import math
import random
import sympy
from decimal import Decimal

# Đổi từ bảng chữ cái sang số
up_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo_alphabet = "abcdefghijklmnopqrstuvwxyz"

up_alphabet_dict = {}
lo_alphabet_dict = {}

for index, letter in enumerate(up_alphabet):
    up_alphabet_dict[letter] = index

for index, letter in enumerate(lo_alphabet):
    lo_alphabet_dict[letter] = index

# Hàm quy đổi hệ chữ cái sang hệ thập phân
def convertName(s:str) -> int:
    sum = 0
    
    for i in range(len(s) - 1, -1, -1):
        sum += lo_alphabet_dict[s[i]] * pow(26, len(s) - 1 - i)    

    return sum

# Thuật toán tìm modulo
def modulo_large_numbers(a, b):
    # Chuyển đổi chuỗi số thành đối tượng Decimal
    a = Decimal(a)
    b = Decimal(b)
    
    # Tính phép chia lấy phần dư
    result = a % b
    
    # Trả về kết quả dưới dạng chuỗi
    return str(result)

# Thuật toán Euclid mở rộng
def extended_euclidian(a, b):
    if b == 0:
        d,x,y = a,1,0
        return [d,x,y]
    
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    
    while b > 0:
        q = a // b
        r = a % b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1 
        y1 = y
    
    d = a
    x = x2
    y = y2
   
    return [d,x,y]

# Thuật toán tính luỹ thừa theo modulo
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

# Thuật toán tìm phi_n (số các số nguyên tố cùng nhau với n mà <= n)
def euler_phi(n):
    if sympy.isprime(n):
        return n - 1
    else:
        factors = sympy.factorint(n)
        result = 1
        for prime, exp in factors.items():
            result *= (prime - 1) * prime ** (exp - 1)
        return result
    
    
while True:
    p = random.randint(10**18, 10**19 - 1)
    if sympy.isprime(p):
        break

while True:
    q = random.randint(10**18, 10**19 - 1)
    if sympy.isprime(q) and q != p:
        break

print("p =", p)
print("q =", q)

n = p * q

print("n: ",n)

# Tìm phi n
phi_n = euler_phi(n)

print("phi_n: ",phi_n)

# Tìm e là số nguyên tố ngẫu nhiên có ít hơn n một chữ số
while True:
    e = random.randint(10**29, 10**30 - 1)
    if sympy.isprime(e):
        break

print("e: ",e)

eList = extended_euclidian(e, phi_n)

d = eList[1]

print("d: ",d)

# Tên sinh viên
name = "daihoccongnghe"

print("Bản tin x: ",name)

# Quy đổi tên sang số trong hệ thập phân
x = convertName(name)

print('Bản rõ x theo modulo n:', modulo_large_numbers(x,n))

# Mã hoá
encryption = modular_exponentiation(x, e, n)

print('Mã hoá:',encryption)

# Giải mã
decryption = modular_exponentiation(encryption, d, n)

print('Giải mã:',decryption)
