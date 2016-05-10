def _choose_topDown(n, k, chooses):
    nk = (n, k)
    if (nk in chooses): return chooses[nk]

    if (n == 0 and k == 0): return 1
    if (k < 0 or k > n): return 0
    result = (_choose_topDown(n - 1, k - 1, chooses) + 
        _choose_topDown(n - 1, k, chooses))
    chooses[nk] = result # save for reuse
    return result

def choose_triangle_topDown(n, k):
    if n < 0 or k < 0:
        raise ValueError
    chooses = {} # hash to avoid recalculation
    return _choose_topDown(n, k, chooses)
