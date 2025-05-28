'''
Write a program to find the number of integers with exactly 9 divisors

Public Test cases:

Input:

100

Output: 2 
36 100

Divisors of 36 = 1, 2, 3, 4, 6, 9, 12, 18, 36 Divisors of 100 = 1, 2, 4, 5, 10, 20, 25, 50, 100
'''

num = int(input())
res = []
count = 0

for i in range(1, num+1):
    if count <= 9:
        if num % i == 0:
            res.append(i)

            count += 1
print(*res) 