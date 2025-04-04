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
'''

n = int(input())
print(bin(n).count('1'))

# or Without using bin function

binary = []
while n > 0:
    remainder = n % 2
    binary.append(remainder)
    n //= 2
print(binary[::-1].count(1))

