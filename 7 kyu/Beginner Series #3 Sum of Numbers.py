def get_sum(a,b):
    box = sorted([a,b])
    if a!=b:
        return sum(range(box[0],box[-1]+1))
    else:
        return a
