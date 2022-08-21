def digital_root(n):
    n = sum([int(i) for i in str(n)])
    if n>=10:
        return digital_root(n)
    else:
        return n
