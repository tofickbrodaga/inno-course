import re

def is_valid_ip(ip):
    pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return True
    else:
        return False

ip = input("Введите ip адрес: ")
if is_valid_ip(ip):
    print("Верный ip адрес")
else:
    print("Неверный ip адрес")