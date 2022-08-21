def delete_nth(order,max_e):
    box = []
    d1 = {k:v for k in order for v in range(1)}
    for val in order:
        if d1[val]!=max_e:
            d1[val]+=1
            box.append(val)
    return box
