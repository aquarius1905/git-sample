# # bytes（変更不可）
# b = b"hello"
# print(b[0])  # => 104
# # b[0] = 72  # ❌ TypeError: 'bytes' object does not support item assignment

# # bytearray（変更可）
# ba = bytearray(b"hello")
# ba[0] = 72
# print(ba)  # => bytearray(b'Hello')
# print(ba.decode())  # => Hello


def modify_data(data: bytearray):
    ba = bytearray(data)  # bytes でも bytearray でも受け取れる
    ba[0] = 72
    return ba


b = b"hello"
result = modify_data(b)  # bytes を渡しても OK
print(result)  # => bytearray(b'Hello')
