from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import elgamal
from cryptography.hazmat.primitives import serialization, hashes
import base64
import time
import random


## Quá trình tiến hành mã hoá, giải mã, ký và kiểm thử chữ ký trên hệ mật ElGamal
## với độ dài khoá 1024 bit


# Tạo cặp khóa ElGamal với p có độ dài 1024 bit
private_key = elgamal.generate_private_key(
    key_size=1024,
    backend=default_backend()
)

# Trích xuất khóa công khai và khóa bí mật
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_key = private_key.public_key()

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Lưu trữ khóa vào file
with open("elgamal_private_key.pem", "wb") as private_file:
    private_file.write(private_pem)

with open("elgamal_public_key.pem", "wb") as public_file:
    public_file.write(public_pem)

print("Quá trình thiết lập khoá, mã hoá và giải mã bằng hệ mật ElGamal:")

time.sleep(2)

# In ra p và g
p = private_key.private_numbers().public_numbers.parameter_numbers.p
g = private_key.private_numbers().public_numbers.parameter_numbers.g

print("p:", p)

time.sleep(2)

print("g:", g)

time.sleep(2)

# Truy cập giá trị x từ khóa bí mật
x = private_key.private_numbers().x

print("x:", x)

time.sleep(2)

# Truy cập giá trị y từ khóa công khai
y = public_key.public_numbers().y

print("y:", y)

time.sleep(2)

# Nội dung bản tin
message = "Chao mung 20 nam thanh lap truong DHCN"

print("Bản tin ban đầu:", message)

# Mã hoá bản tin
k = random.randint(2, p - 2)
ciphertext = public_key.encrypt(
    message.encode('utf-8'),
    elgamal.ElGamalCiphertext(
        bytes([random.randint(1, 255) for _ in range(128)]),
        bytes([random.randint(1, 255) for _ in range(128)])
    ),
    k
)

print("Bản tin đã mã hóa:", base64.b64encode(ciphertext).decode('utf-8'))

time.sleep(2)

# Giải mã bản tin
plaintext = private_key.decrypt(
    ciphertext,
    elgamal.ElGamalCiphertext(
        bytes([random.randint(1, 255) for _ in range(128)]),
        bytes([random.randint(1, 255) for _ in range(128)])
    )
)

print("Bản tin đã giải mã:", plaintext.decode('utf-8'))