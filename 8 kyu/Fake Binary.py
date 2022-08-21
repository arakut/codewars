def fake_bin(x):
    box = []
    for num in x:
        if int(num)<5:
            box.append('0')
        else:
            box.append('1')
    return ''.join(box)
