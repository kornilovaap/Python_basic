simple_string = "Hello, world!"
byte_string = b"Hello, world!"
byte_array_string = bytearray(byte_string)

print(byte_string)
print(type(simple_string))
print(type(byte_string))
print(type(byte_array_string))

name = "John"
byte_name = name.encode()  # по умолчанию utf-8
print(type(byte_name))
