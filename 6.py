import array
import binascii

arr = array.array('i', [1,2,3,4,5,6])
print("Original array:")
print('A1:', arr)

array_bytes = arr.tobytes()
print('Array of bytes:', binascii.hexlify(array_bytes))