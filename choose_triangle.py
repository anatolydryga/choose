def _choose_triangle_recursive(n, k):
    if (n == 0 and k == 0): return 1
    if (k < 0 or k > n): return 0
    return (_choose_triangle_recursive(n - 1, k - 1) + 
        _choose_triangle_recursive(n - 1, k))

def choose_triangle_recursive(n, k):
    if n < 0 or k < 0:
        raise ValueError
    return _choose_triangle_recursive(n, k)
