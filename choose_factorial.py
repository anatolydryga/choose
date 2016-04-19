def factorial(n):
# recursive implementation: hits maximum recursion depth(e.g. n 1000)
#    if n == 0: return 1
#    return n*factorial(n - 1)

# iterative implementation
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def choose_factorial(n, k):
    if n < 0 or k < 0:
        raise ValueError
    if k > n: return 0
    #return factorial(n) / factorial(k) * factorial(n-k) # !BUG! operator precedence
    return factorial(n) / factorial(k) / factorial(n-k)
