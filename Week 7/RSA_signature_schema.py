import sympy
import random
import time


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dict = {}

for index, letter in enumerate(alphabet):
    alphabet_dict[letter] = index

def convertName(s:str) -> int:
    sum = 0
    
    for i in range(len(s) - 1, -1, -1):
        sum += alphabet_dict[s[i]] * pow(26, len(s) - 1 - i)    

    return sum

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

def euler_phi(n):
    if sympy.isprime(n):
        return n - 1
    else:
        factors = sympy.factorint(n)
        result = 1
        for prime, exp in factors.items():
            result *= (prime - 1) * prime ** (exp - 1)
        return result
    
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

### Qúa trình kí và xác thực
print("Sơ đồ chữ ký RSA")

time.sleep(1)

# Phần việc của Bob
print("Các tham số của hệ mật mã công khai S1:")

time.sleep(0.5)

print("Ở đây, Bob sẽ tạo ra hai số nguyên tố p và q")

p = 4933
q = 5441

n = p * q

print(f"p = {p}")

time.sleep(0.5)

print(f"q = {q}")

print("Sau đó tính n")

time.sleep(0.5)

print(f"n = pq = {n}")

phi_n = euler_phi(n)

time.sleep(0.5)

print(f"phi_n = {phi_n}")

check = False

while check is False:
    while True:
        e = random.randint(10**7,n)
        
        if sympy.isprime(e):
            break 

    ee = extended_euclidian(e, phi_n)
    d = ee[1]
    
    if d > 0:
        check = True

print(f"e = {e}")

time.sleep(0.5)

print(f"d = {d}")

time.sleep(2)

# Phần việc của Alice
print("Các tham số cho hệ xác nhận bằng chữ ký S2:")

while True:
    p1 = random.randint(3*10**3,10**4 - 1)
    
    if sympy.isprime(p1):
        break 

time.sleep(0.5)

print(f"p = {p1}")

while True:
    q1 = random.randint(4*10**3,10**4 - 1)
    
    if sympy.isprime(q1):
        break 

time.sleep(0.5)

print(f"q = {q1}")

time.sleep(0.5)

n1 = p1 * q1

print(f"n = pq = {n1}")

phi_n1 = euler_phi(n1)

print(f"phi_n = {phi_n1}")

check = False

while check is False:
    while True:
        a = random.randint(10**7,phi_n1)
        
        if sympy.isprime(a):
            break 

    ee2 = extended_euclidian(a, phi_n1)
    b = ee2[1]

    if b > 0:
        check = True
        
print(f"a = {a}")

time.sleep(0.5)

print(f"b = {b}")

print("Sơ đồ chữ ký RSA gồm hai hệ mật khoá công khai S1 và hệ xác nhận bằng chữ ký S2")

time.sleep(1)

print(f"B có bộ khoá mật mã K = (K', K''), với khoá công khai K' = (n,e) = ({n}, {e}) và khoá bí mật K'' = d = {d} trong hệ S1")

time.sleep(1)

print(f"A có bộ khoá chữ ký K_s = (K_s', K_s''), với khoá công khai K_s' = b = {b} và khoá bí mật K_s'' = (n,a) = ({n1}, {a}) trong hệ S2")

x = "YHUNG"

time.sleep(1)

print(f"Bản tin x = {x}")

convertSum = convertName(x)

time.sleep(1)

print("Mã hoá bản tin x, ở đây Alice sẽ mã hoá bản tin x bằng khoá công khai của Bob:")

encryption = modular_exponentiation(convertSum,e,n)

print(f"Bản mã: {encryption}")

time.sleep(1)

sign = modular_exponentiation(convertSum,a,n1)

print(f"Alice tạo chữ ký bằng khoá bí mật của mình, sign = {sign}")

time.sleep(1)

print("Bob nhận được cặp mã hoá kèm chữ ký từ Alice")

time.sleep(1)

print("Tiến hành giải mã bằng khoá bí mật của Bob:")

decryption = modular_exponentiation(encryption,d,n)

time.sleep(1)

print(f"Bản tin sau khi được giải mã:{decryption}")

time.sleep(1)

print("Kiểm tra chữ ký bằng khoá công khai của Alice:")

ver = modular_exponentiation(sign,b,n1)

print(f"ver = {ver}")

if sign == ver:
    print("Xác thực chính xác, người gửi là Alice")
else:
    print("Xác thực không chính xác, người gửi không phải Alice")