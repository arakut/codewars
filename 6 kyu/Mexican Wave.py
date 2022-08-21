def wave(people):
    box = []
    for val in range(len(people)):
        if people[val].isalpha():
            box.append(people[:val]+people[val].capitalize()+people[val+1:])
    return box
