# byte= b'abcd\x65'
# print ("Given Byte is :",byte)
# print ("Type of byte is :", type(byte))
# print ("Byte[2] is :", byte[2])
# print ("Length of byte before concat is  :" ,len(byte))
# byte=byte + b'\x66'
# print ("New byte is :" ,byte)
# print ("Length of byte after concat is :" ,len(byte))
# byte_arr=bytearray(byte)
# byte_arr[0]=102
# print



a_string = '90 Python'
print (len(a_string))
by = a_string.encode('utf-8')
print (by)
by=a_string.encode('gb18030')
print(by)
by = a_string.encode('big5')
print(by)
roundtrip = by.decode('big5')
print(roundtrip)

