'''
Problem Statement -: In this even odd problem Given a range [low, high] (both inclusive), select K numbers from the range 
(a number can be chosen multiple times) such that sum of those K numbers is even.

Calculate the number of all such permutations.

As this number can be large, print it modulo (1e9 +7).

Constraints

0 <= low <= high <= 10^9
K <= 10^6.
Input

First line contains two space separated integers denoting low and high respectively
Second line contains a single integer K.
Output

Print a single integer denoting the number of all such permutations
Time Limit

1

Examples

Example 1

Input

4 5

3

Output

4

Explanation

There are 4 valid permutations viz. {4, 4, 4}, {4, 5, 5}, {5, 4, 5} and {5, 5, 4} which sum up to an even number.

Example 2

Input

1 10

2

Output

50

Explanation

There are 50 valid permutations viz. {1,1}, {1, 3},.. {1, 9} {2,2}, {2, 4},… {2, 10} . . . {10, 2}, {10, 4},… {10, 10}. These 50 permutations, each sum up to an even number.

'''

MOD = int(1e9 + 7)

def mod_inv(n, mod):
    """Computes modular inverse of n under modulo mod using Fermat's Theorem."""
    return pow(n, mod - 2, mod)

def precompute_factorials(n, mod):
    """Precompute factorials and their modular inverses up to n."""
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    inv_fact[n] = mod_inv(fact[n], mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    return fact, inv_fact

def binomial(n, k, fact, inv_fact, mod):
    """Computes binomial coefficient C(n, k) % mod."""
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def count_even_sum_permutations(low, high, K):
    """Count the number of valid permutations where sum is even."""
    e_count = len([x for x in range(low, high + 1) if x % 2 == 0])
    o_count = (high - low + 1) - e_count  # Remaining are odd

    if K == 1:
        return e_count % MOD  # Only even numbers form valid permutations

    fact, inv_fact = precompute_factorials(K, MOD)

    result = 0
    for x in range(0, K + 1, 2):  # Pick even `x`
        y = K - x
        ways = binomial(K, x, fact, inv_fact, MOD)  # Choose `x` positions for evens
        ways = (ways * pow(e_count, x, MOD)) % MOD  # Assign evens
        ways = (ways * pow(o_count, y, MOD)) % MOD  # Assign odds
        result = (result + ways) % MOD
    
    return result

# Input
low, high = map(int, input().split())
K = int(input())

# Output result
print(count_even_sum_permutations(low, high, K))
