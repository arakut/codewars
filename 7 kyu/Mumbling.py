def accum(s):
    d1 = {k:v for k,v in enumerate(s, start= 1)}
    box = []
    for val in range(1, len(d1)+1):
        var = d1[val]*val
        box.append(var.title())
    return '-'.join(box)
