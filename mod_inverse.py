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

# Sử dụng hàm mod_inverse để tính phần tử nghịch đảo của a trong modulo n
a = 7  # Thay đổi giá trị của a theo yêu cầu của bạn
n = 11  # Thay đổi giá trị của n theo yêu cầu của bạn

try:
    inverse_a = mod_inverse(a, n)
    print(f'Phần tử nghịch đảo của {a} trong modulo {n} là {inverse_a}')
except Exception as e:
    print(e)
