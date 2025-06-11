# Initialize numbers (shown in binary comments)
a = 10    # 1010 in binary
b = 4     # 0100 in binary

# Bitwise AND (&)
bit_and = a & b    # 1010 & 0100 = 0000 (0)
print('Bitwise AND (10 & 4):', bit_and)  # 0

# Bitwise OR (|)
bit_or = a | b     # 1010 | 0100 = 1110 (14)
print('Bitwise OR (10 | 4):', bit_or)    # 14

# Bitwise XOR (^)
bit_xor = a ^ b    # 1010 ^ 0100 = 1110 (14)
print('Bitwise XOR (10 ^ 4):', bit_xor)  # 14

# Bitwise NOT (~)
bit_not = ~a       # ~00001010 = 11110101 (-11 in two's complement)
print('Bitwise NOT (~10):', bit_not)     # -11

# Left Shift (<<)
left_shift = a << 2  # 1010 << 2 = 101000 (40)
print('Left Shift (10 << 2):', left_shift)  # 40

# Right Shift (>>)
right_shift = a >> 1  # 1010 >> 1 = 0101 (5)
print('Right Shift (10 >> 1):', right_shift)  # 5
