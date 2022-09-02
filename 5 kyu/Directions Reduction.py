def dirReduc(arr):
    directions = ["NORTH", "WEST", "SOUTH", "EAST"]
    directions_dict = dict(zip(directions, [1,2,-1,-2]))
    way = [directions_dict[i] for i in arr]
    inv_directions_dict = dict(zip([1,2,-1,-2], directions))
    num = 0
    try:
        while True:
            if way[num]+way[num+1]==0:
                way.pop(num+1)
                way.pop(num)
                num = 0
            else:
                num+=1
    except:
        return [inv_directions_dict[i] for i in way]

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
b = ['SOUTH', 'SOUTH', 'NORTH', 'WEST', 'EAST', 'WEST', 'SOUTH', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST', 'SOUTH', 'WEST', 'SOUTH', 'SOUTH', 'NORTH', 'SOUTH']

print(dirReduc(b))
