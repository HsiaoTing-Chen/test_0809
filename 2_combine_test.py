def C(n,r):
    if r == 1:
        return n
    elif r == n:
        return 1 
    else:
        return C(n-1,r) + C(n-1, r-1)
c = C(990,33)
print(c)
