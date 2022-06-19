# coding: utf-8
def fac(z):
    if len(z) == 1:
    # The base case for escaping the recursive loop
        return z
    a = []
    for i in range(len(z)):
        c = z[:i] + z[i+1:]
        d = fac(c)
        for y in d:
            a.append(z[i] + y)
    return a
    
