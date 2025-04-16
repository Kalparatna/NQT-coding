'''
Shift-1
Q1)You are given two integers m and n. Your task is to compute the sum of the m-th prime number to the (m + n)-th prime
number, inclusive.

Input:
Two integers m and n such that m ≥ 1 and n ≥ 0
Output:
Print the sum of the m-th, (m+1)-th. ... , (mtn)-th prime numbers.
Example 1:
Input:
m= 2
n= 2

Output:
Sum = 15

Explanation:
2nd prime = 3
3rd prime = 5
4th prime = 7
Sum = 3 + 5 + 7 = 15

eg-2
Input:
m = 1
n = 3

Explanation: We need the sum of 1st, 2nd, 3rd, and 4th prime numbers.

1st prime = 2
2nd prime = 3
3rd prime = 5
4th prime = 7
Sum = 2 + 3 +5 + 7 = 17

'''
def is_prime(n):
    if n ==0 or n==1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            return False
        
    return True

m,n = map(int, input().split())
sum_prime = 0
count = 0
i = 2

while count < m+n:
    if is_prime(i):
        count += 1
        if count >= m:
            sum_prime += i
    i += 1

print(sum_prime)
