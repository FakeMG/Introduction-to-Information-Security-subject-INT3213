import random
from sympy import isprime

# Hàm sinh số nguyên tố có độ dài xác định
def generate_prime(bit_length):
    while True:
        p = random.getrandbits(bit_length)
        if isprime(p):
            return p

# Nhập độ dài của số nguyên tố p (khoảng 160 bit)
print("Nhập độ dài của p (khoảng 160 bit):")
bit_length = int(input())

p = generate_prime(bit_length)
print("p =", p)

found = False

while not found:
    # Tạo ngẫu nhiên giá trị a và b nằm trong trường hữu hạn
    a = random.randint(0, 79)
    b = random.randint(0, 79)

    # Kiểm tra điều kiện 4a^3 + 27b^2 ≠ 0 (mod p)
    if (4 * (a**3) + 27 * (b**2)) % p != 0:
        
        # Đếm số điểm trên đường cong elliptic
        count = 0
        for x in range(p):
            y_squared = (x**3 + a * x + b) % p
            
            # Kiểm tra xem y_squared thuộc tập các phần tử thặng dư bậc 2 Q_p hay không
            if (y_squared ** ((p - 1) // 2)) % p == 1:
                count += 2  # Đếm số điểm, không cần kiểm tra số nguyên tố

        # Kiểm tra xem số điểm trên đường cong có phải là số nguyên tố
        if isprime(count + 1):
            found = True

print(f"Tìm thấy đường cong elliptic:")
print(f"a = {a}, b = {b}")
print(f"Tổng số điểm trên đường cong: {count + 1}")