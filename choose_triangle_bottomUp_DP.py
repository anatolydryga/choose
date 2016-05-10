import numpy

def choose_triangle_bottomUp(n, k):
    if n < 0 or k < 0:
        raise ValueError
    chooses = numpy.zeros((n + 1, k + 1))
    chooses[0:n + 1, 0] = 1
    for i in range(0, n + 1):
        for j in range(1, i + 1):
            if j > k: break
            chooses[i, j] = chooses[i - 1, j - 1] + chooses[i - 1, j]
    return chooses[n, k] 
