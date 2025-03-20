'''
Write a function to return position of first 1 from right to left, in binary representation of an Integer.

I/P 18, Binary Representation 010010

O/P

2

I/P 19, Binary Representation 010011

O/P 1
'''
# Rightmost 1
num = int(input())

position = 1

while num > 0:
    if num & 1 == 1:
        print(position)
        break
    num >>= 1
    position += 1

#left most 1
'''

def leftmost_set_bit_position(num):
    if num == 0:
        return -1  # No set bit in 0

    position = 0  # Bit position tracker

    while num > 0:
        position += 1
        num >>= 1  # Right shift the number until only the leftmost '1' remains

    return position

# Example usage:
num = int(input("Enter a number: "))
print(leftmost_set_bit_position(num))

'''

    