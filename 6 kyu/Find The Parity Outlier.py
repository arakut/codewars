def find_outlier(integers):
    chet = [i for i in integers if i%2==0]
    nechet = [i for i in integers if i%2==1]
    return chet[0] if len(chet)<len(nechet) else nechet[0]
