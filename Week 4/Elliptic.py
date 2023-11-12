import random
import sympy

# Đổi từ bảng chữ cái sang số
up_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

up_alphabet_dict = {}

for index, letter in enumerate(up_alphabet):
    up_alphabet_dict[letter] = index
    
# Hàm quy đổi hệ chữ cái sang hệ thập phân
def convertUpperName(s:str) -> int:
    sum = 0
    
    for i in range(len(s) - 1, -1, -1):
        sum += up_alphabet_dict[s[i]] * pow(26, len(s) - 1 - i)    

    return sum

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


def binary_to_decimal(binary_str):
    try:
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError:
        print("Lỗi: Chuỗi không phải là số nhị phân.")
        return None


len = int(input("Mời nhập số chữ số của p:"))

while True:
    p = random.randint(10**(len - 1), 10**len - 1)
    if sympy.isprime(p):
        break

print("Ta có p = ", p)

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
        if sympy.isprime(count + 1):
            found = True

print(f"Tìm thấy đường cong elliptic:")
print(f"a = {a}, b = {b}")
print(f"Tổng số điểm trên đường cong: {count + 1}")

message = 'HUN'

convertSum = convertUpperName(message)

binSum = format(convertSum,'b')

print(binSum)

# Vì số này chỉ có độ dài 13 bit nên em sẽ tiến hành thêm vào số khác để cho đủ độ dài 15 bit

new_binSum = "110100100100010"

x_test = binary_to_decimal(new_binSum)

y_test = (x_test**3 + a * x + b) % p

if y_test in blList:
    print(f"Ta có điểm P({x_test},{y_test}) có thuộc trên đường cong Elliptic E")
else:
    print("Thử lại")