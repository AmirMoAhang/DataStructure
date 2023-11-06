def Combination(n, k):
    if n==k or k ==0:
        return 1
    return Combination(n - 1, k) + Combination(n - 1, k - 1)