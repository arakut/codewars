import string

def high(x):
    alph_dict = {k:v for v,k in enumerate(string.ascii_lowercase,start = 1)}
    box = [0, None]
    for item in x.split():
        count = 0
        for val in item:
            count+=alph_dict.get(val)
        if count>box[0]:
            box[0] = count
            box[1] = item
    return box[-1]
