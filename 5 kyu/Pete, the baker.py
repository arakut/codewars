def cakes(recipe, available):
    box = []
    for elem in recipe:
        try:
            box.append(available[elem]//recipe[elem])
        except:
            box.append(0)
    return min(box)
