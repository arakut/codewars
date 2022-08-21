def duplicate_encode(word):
    word_dict = {k:v for k in [i.lower() for i in word] for v in range(0,1)}
    box = []
    for item in word:
        word_dict[item.lower()]+=1
    for item in word:
        if word_dict[item.lower()]>1:
            box.append(')')
        else:
            box.append('(')
    return ''.join(box)
