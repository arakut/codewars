import random

def anagrams(word, words):
    box = []
    box1= []
    l1 = list(word)
    for i in range(150):
        random.shuffle(l1)
        if ''.join(l1) not in box:
            box.append(''.join(l1))
    for c in words:
        if c in box:
            box1.append(c)
    return box1
