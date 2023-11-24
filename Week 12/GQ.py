import time
import random
import sympy


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
        raise Exception('Phần tử nghịch đảo không tồn tại')
    else:
        return x % m


print("Sơ đồ xưng danh Guillou-Quisquater")

time.sleep(2)

print("TA chọn hai số nguyên tố p và q")

p = 4933
q = 5441

time.sleep(2)

print(f"Ta có p = {p}, q = {q}")

n = p * q

time.sleep(1)

print(f"Ta có n = {n}")

time.sleep(2)

print("TA cũng chọn thêm một số b là số nguyên tố")

while True:
    b = random.randint(10**7, 7 * 10**7)
    
    if sympy.isprime(b):
        break

time.sleep(2)

print(f"Ta có b = {b}")

time.sleep(2)

print("Thủ tục cấp chứng chỉ cho một người tham gia A được tiến hành như sau:")

time.sleep(2)

print("1. TA xác lập các thông tin về danh tính của A dưới dạng một dãy ký tự mà ta ký hiệu là I_A hay ID(A)")

time.sleep(2)

print("2. A chọn bí mật một số ngẫu nhiên u (0 <= u <= n-1), tính v = (u ^-1) ^ b mod n, sau đó chuyển số v cho TA")

while True:
    u = random.randint(0, n - 1)
    
    if sympy.isprime(u):
        break
    
v = modular_exponentiation(mod_inverse(u, n),b,n)

time.sleep(1.5)

print("3. TA tạo chữ ký s = sig_TA(I_A,v) và cấp cho A chứng chỉ C(A) = (ID(A), v, s)")

time.sleep(2)

print("Bây giờ, với chứng chỉ C(A) đó, A có thể xưng danh với bất kỳ đối tác B nào bằng cách cùng B thực hiện một giao thức xác nhận danh tính như sau:")

time.sleep(2)

print("1. A chọn thêm một số ngẫu nhiên k (0 <= k <= n - 1), tính gamma = k^b modn")

time.sleep(3)

print("và gửi cho B các thông tin C(A) và gamma")

while True:
    k = random.randint(0, n - 1)
    
    if sympy.isprime(k):
        break

gamma = modular_exponentiation(k,b,n)

time.sleep(2)

print("2. B kiểm thử chữ ký của TA trong chứng chỉ C(A) bởi hệ thức verTA(ID(A), v, s) = đúng.")

time.sleep(3)

print("Kiểm thử xong, B chọn một số ngẫu nhiên r (1 <= r <= b - 1) và gửi r cho A.")

while True:
    r = random.randint(1, b - 1)
    
    if sympy.isprime(r):
        break
    
time.sleep(2)

print("3. A tính y = k.u^r mod n và gửi y cho B")

y = modular_exponentiation(u,r,n)

y = modular_exponentiation(k * y,1,n)

time.sleep(2)

print("4. B thử điều kiện gamma === v^r . y^b (modn)")


