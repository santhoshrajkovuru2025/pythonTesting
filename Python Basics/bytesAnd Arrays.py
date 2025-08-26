

# Till 255 we can give the values in the bytes and byte arrays
# No assignment of the values allowed in bytes, but we can any value in byte array
# No Slicing and repetition is allowed for both the bytes and bytes arrays


lst=[1,15,22,33,154,234,255]

print(type(lst))

byte=bytes(lst)
print(type(byte))


byteA=bytearray(lst)
print(type(byteA))
byteA[5]=55
print(byteA)



