# start the value as string
value = "hello"
print(value)
value = value.encode('utf-8')
print(value)

# conmvert to byte array
value = bytearray(value)
print(value)

# add in anotehr character
value.append(67)

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

# decode it
value = value.decode("utf-8")
print(value)