import random
import sympy
from sympy import isprime

# Hàm tính modulo theo số mũ
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

print("Ta có p = 79")
p = 79

found = False

while not found:
    # Tạo ngẫu nhiên giá trị a và b nằm trong trường hữu hạn
    a = random.randint(1,78)
    b = random.randint(1,78)

    # Kiểm tra điều kiện 4a^3 + 27b^2 ≠ 0 (mod 79)
    if (4 * (a**3) + 27 * (b**2)) % p != 0:
        
        blList = []
        
        for i in range(1, int((p + 1) / 2), 1):
            blList.append(modular_exponentiation(i,2,p))
            
        # Đếm số điểm trên đường cong elliptic
        count = 0
        
        for x in range(p):
            y_squared = (x**3 + a * x + b) % p
            
            if y_squared in blList:   
                count += 2  # Đếm số điểm, không cần kiểm tra số nguyên tố

        # Kiểm tra xem số điểm trên đường cong có phải là số nguyên tố
        if isprime(count + 1):
            found = True

print(f"Tìm thấy đường cong elliptic:")
print(f"a = {a}, b = {b}")
print(f"Tổng số điểm trên đường cong: {count + 1}")