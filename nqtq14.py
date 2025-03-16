'''
Given two numbers M and N. The task is to find the position of rightmost different bit in binary representation of numbers.

Input:

Two space separated integers M and N.

Output:

Print the position of rightmost different bit in binary representation of numbers.

Constraints:

1 <= M <= 103

1 <= N <= 103

M and N takes different Values

Example:

Input:

11 9

52 4

Output: 
2 
5
'''

def righ_most_bit(M, N):
    xor_op = M ^ N
    position = 1
    while xor_op > 0:
        if xor_op & 1 == 1:
            return position
        
        xor_op >>= 1
        position += 1
    
    return -1


M, N = map(int, input().split())

print(righ_most_bit(M, N))

