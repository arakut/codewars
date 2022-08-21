def in_array(ar1, ar2):
    arr3 = []   
    for word1 in ar1:
        for word2 in ar2:
            if word1 in word2 and word1 not in arr3:
                arr3.append(word1)
    return sorted(arr3)
