'''
Sum of All Prime Numbers Between 2 and n
Given an integer n, return the sum of all prime numbers between 2 and n (inclusive).
Constraints:

Input:
A single integer n representing the upper limit.
Output:
Return an integer representing the sum of all prime numbers between 2 and n.
Example 1:
Input: 10
Output: 17
Explanation: The prime numbers between 2 and 10 are [2, 3, 5, 7]. Their sum is 2 + 3 + 5 + 7 = 17.
Example 2:
Input: 2
Output: 2
Explanation: 2 is the only prime number between 2 and 2.

'''

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input())
primesum = 0
for i in range(2, num + 1):
    if isPrime(i):
        primesum += i

print(primesum)
