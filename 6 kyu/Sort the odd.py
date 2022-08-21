def sort_array(source_array):
    even_box = sorted([i for i in source_array if i%2!=0])
    count = 0
    for num in range(len(source_array)):
        if source_array[num] in even_box:
            source_array[num] = even_box[count]
            count+=1
    return source_array
