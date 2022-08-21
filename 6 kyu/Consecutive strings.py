def longest_consec(strarr, k):
    if k<0 or len(strarr)<k or len(strarr)==0:
        return ''
    else:
        box = []
        for elem in range(len(strarr)):
            box.append(''.join(strarr[elem:k]))
            k+=1
        box.sort(key=lambda x: len(x), reverse = True)
        return box[0]
