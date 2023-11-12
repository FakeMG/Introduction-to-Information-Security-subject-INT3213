from decimal import Decimal

def modulo_large_numbers(a, b):
    # Chuyển đổi chuỗi số thành đối tượng Decimal
    a = Decimal(a)
    b = Decimal(b)
    
    # Tính phép chia lấy phần dư
    result = a % b
    
    return result

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dict = {}

for index, letter in enumerate(alphabet):
    alphabet_dict[letter] = index

def convertName(s:str) -> int:
    sum = 0
    
    for i in range(len(s) - 1, -1, -1):
        sum += alphabet_dict[s[i]] * pow(26, len(s) - 1 - i)    

    return sum


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


def ElGamalEncryption(p, alpha, beta, x, k):
    y1 = modular_exponentiation(alpha, k, p)
    
    y2 = modular_exponentiation(beta, k, p)
    y2 = modulo_large_numbers(y2 * x, p)
    
    return [y1, y2]
    
def ElGamalDecryption(y1, y2, a, p):
    result =  modular_exponentiation(y1, p - a - 1, p)
    
    result = modulo_large_numbers(result * y2, p)
    
    return result
    
p = 4942901017
alpha = 5
a = 888
beta = 4242210690
k = 29102002

name = "NGUYENDUYHUNG"

x = convertName(name)

print('Bản mã x:', modulo_large_numbers(x, p))

encryption = ElGamalEncryption(p, alpha, beta, x, k)

print("Mã hoá:", encryption)

y1 = encryption[0]
y2 = encryption[1]

print("Giải mã:", ElGamalDecryption(y1, y2, a, p))