'''
Given a positive integer N, print count of set bits in it.

Example 1:

Input:

N=6

Output:

2

Explanation:

Binary representation is '110'

So the count of the set bit is 2.

Example 2:

Input:

8

Output:

1

Explanation:

Binary representation is '1000'

So the count of the set bit is 1.
Subtracting 1 from a decimal number flips all the bits after the rightmost set bit(which is 1) including the rightmost set bit.

For example:


BriN kernighans algorithm 

0 0000

10 in binary is 00001010

مد 0001

9 in binary is 00001001

2

0010

8 in binary is 00001000

7 in binary is 00000111

So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit. If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.

The beauty of this solution is the number of times it loops is equal to the number of set bits in a given integer.

'''

num = int(input())

converted = bin(num)
binarystr = converted[2:]
i = 2
res = 0
for i in binarystr:
    if i == '1':
        res += 1

print(res)

# or Using  BriN kernighans algorithm 


'''
def count_set_bits(n):
    count = 0
    while n > 0:
        # Perform n = n & (n - 1) to unset the rightmost set bit
        n = n & (n - 1)
        count += 1
    return count

# Example input
num = 8
result = count_set_bits(num)

print("Count of set bits:", result)
'''