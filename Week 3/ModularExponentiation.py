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

a = 5
b = 888
n = 4942901017

print("alpha_'",modular_exponentiation(a,b,n))

name = "NGUYENDUYHUNG"
x = convertName(name)
x1 = 5234673
phiN = 6007800
d = 422191
e = 3674911
n = 6012707

print(x)

print(modular_exponentiation(x,e,n))

y = modular_exponentiation(x,e,n)

print(modular_exponentiation(y,d,n))