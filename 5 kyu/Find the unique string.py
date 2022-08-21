def find_uniq(arr):
    arr1 = ''.join(arr).lower()
    d1 = {k:v for k in arr1 for v in range(1)}
    for val in arr1:
        d1[val]+=1
    t1 = [*d1.items()]
    answ = sorted(t1,key=lambda t1: t1[-1])[0][0]
    for val in arr:
        if answ.lower() in val or answ.upper() in val:
            return val
