def find_uniq(arr):
    set_1 = set(arr)
    for num in set_1:
        if arr.count(num)==1:
            return num
