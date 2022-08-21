def tower_builder(n_floors):
    box = []
    for lvl in range(n_floors):
        box.append(' '*(n_floors-lvl-1)+'*'*(lvl+1)+'*'*lvl+' '*(n_floors-lvl-1))
    return box
