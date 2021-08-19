# start the value as integer
value = 123456789
print(value)
# convert to bitstring
value = bin(value)[2:]
print(value)

# function to convert bitstring to bytearray
def convert_string_byte(new_value):
    current_value = bytearray()
    for i in range(0, len(new_value), 8):
        current_value.append(int(new_value[i:i+8],2))
    return current_value
value = convert_string_byte(value)
print(value)

# write to binary file
filename = "binary_file.bin"
print(value)
write_file = open(filename, "wb")
write_file.write(value)
write_file.close()

# read from binary file
read_file = open(filename, "rb")
value = read_file.read()
read_file.close()
print(value)

# convert to bytearray
value = bytearray(value)

# convert to bitstring
temp = ""
for i in range(len(value)):
    if i < len(value)-1:
        temp = temp + format(value[i], '08b')
    else:
        temp = temp + bin(value[i])[2:]
value = temp
print(value)

# convert to int
value = int(value, 2)
print(value)