def count_positives_sum_negatives(arr):
    result = []
    pos = sum([1 for i in arr if i>0])
    result.append(pos)
    negat = sum([i for i in arr if i<0 and i!=0])
    result.append(negat)
    if arr==[]:
        return []
    else:
        return result
