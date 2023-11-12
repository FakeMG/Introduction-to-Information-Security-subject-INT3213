from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
import base64
import time


## Quá trình mã hoá, giải mã, ký và kiểm thử chữ ký trên hệ mật RSA
## với độ dài 3072 bit


# Tạo cặp khóa RSA với n có độ dài 3072 bit
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Exponent e
    key_size=3072,  # Độ dài khóa n
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
with open("private_key.pem", "wb") as private_file:
    private_file.write(private_pem)

with open("public_key.pem", "wb") as public_file:
    public_file.write(public_pem)

print("Quá trình thiết lập mã hoá và giải mã bằng hệ mật RSA:")

time.sleep(2)

# In ra p và q
p = private_key.private_numbers().p
q = private_key.private_numbers().q

print("p:", p)

time.sleep(2)

print("q:", q)

time.sleep(2)

# Tính n và phi_n
n = p * q
phi_n = (p - 1) * (q - 1)

print("n:", n)

time.sleep(2)

print("phi_n:", phi_n)

time.sleep(2)

# Truy cập giá trị e từ khóa công khai
e = public_key.public_numbers().e

# Truy cập giá trị d từ khóa bí mật
d = private_key.private_numbers().d

print("e:", e)

time.sleep(2)

print("d:", d)

time.sleep(2)

time.sleep(2)

# Nội dung bản tin
message = "Chao mung 20 nam thanh lap truong DHCN"

print("Bản tin ban đầu:",message)

# Mã hoá bản tin
encrypted_message = public_key.encrypt(
    message.encode('utf-8'),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Giải mã bản tin
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# In ra kết quả
print("Bản tin đã mã hóa:", base64.b64encode(encrypted_message).decode('utf-8'))

time.sleep(2)

print("Bản tin đã giải mã:", decrypted_message.decode('utf-8'))

time.sleep(2)

# Hàm tạo chữ ký
def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

print("Quá trình thiết lập sơ đồ chữ ký bằng hệ mật RSA:")

time.sleep(2)

# Kí và in chữ ký
signature = sign_message(private_key, message)
print("Chữ ký:", base64.b64encode(signature).decode('utf-8'))


# Hàm kiểm thử chữ ký
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Lỗi xác thực chữ ký: {e}")
        return False

time.sleep(2)

print("Tiến hành kiểm thử chữ ký:")

time.sleep(2)

# Kiểm thử chữ ký
if verify_signature(public_key, message, signature):
    print("Chữ ký hợp lệ.")
else:
    print("Chữ ký không hợp lệ.")
    
time.sleep(1)

print("Chúc mừng bạn đã thiết lập thành công hệ mật RSA!")