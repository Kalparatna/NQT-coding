'''
Given a positive integer, N) Find the factorial of N.

Example 1:

Input:

N=5

Output:

120

Explanation:

5*4*3*2*1 = 120

Iteration

2 Recusion

} data types

3

Example 2:

Input:

N=4

Output:

24

Explanation:

4*3*2*124

'''

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

num = int(input())
print(f"Factorial of Num : ", factorial(num))