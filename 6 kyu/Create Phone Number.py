def create_phone_number(n):
    r =  []
    for num in n:
        r.append(str(num))
    q = ''.join(r[:3])
    w = ''.join(r[3:6])
    e = ''.join(r[-4:])
    return f'({q}) {w}-{e}
