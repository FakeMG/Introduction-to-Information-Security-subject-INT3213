from decimal import Decimal

def modulo_large_numbers(a, b):
    # Chuyển đổi chuỗi số thành đối tượng Decimal
    a = Decimal(a)
    b = Decimal(b)
    
    # Tính phép chia lấy phần dư
    result = a % b
    
    # Trả về kết quả dưới dạng chuỗi
    return str(result)

# Sử dụng hàm với số lớn
a = "1265553094422427648"  # 50 chữ số
b = "5472735423886121"  # 50 chữ số

result = modulo_large_numbers(a, b)
print(result)
