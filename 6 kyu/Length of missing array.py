def get_length_of_missing_array(array_of_arrays):
    try:
        some_list = sorted([len(i) for i in array_of_arrays])
        elements = [i for i in range(min(some_list),max(some_list)+1)]
        for num in elements:
            if num not in some_list:
                print(some_list)
                return num
            elif num==0:
                return 0
    except:
        return 0
