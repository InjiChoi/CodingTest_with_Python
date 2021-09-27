# https://www.acmicpc.net/problem/10930
# SHA-256
# 해시, 구현
import hashlib

input_data = input()
encoded_data = input_data.encode()  # byte 객체 구하기
result = hashlib.sha256(encoded_data).hexdigest()
print(result)
