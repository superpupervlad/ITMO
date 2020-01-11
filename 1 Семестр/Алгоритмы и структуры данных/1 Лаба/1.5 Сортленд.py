def merge(left,right):
    a = []
    while (len(left)*len(right)>0):
        if left[0] < right[0]:
            a.append(left[0])
            left.pop(0)
        else:
            a.append(right[0])
            right.pop(0)
    if (len(left) > 0):
        for i in range(len(left)):
            a.append(left[0])
            left.pop(0)
    if (len(right) > 0):
        for i in range(len(right)):
            a.append(right[0])
            right.pop(0)
    return a
        
def s(array):
    if len(array) == 1:
        return array
    if len(array) > 2:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]
        left_array = s(left_array)
        right_array = s(right_array)
        return(merge(left_array,right_array))
    if len(array) == 2:
        if array[1] < array[0]:
            array[0],array[1] = array[1],array[0]
        return(array)
    
            
fin = open("sortland.in")
fout = open("sortland.out", "w")
n = map(int, fin.readline().split())
array = list(map(float, fin.readline().split()))
array_b = tuple(array)
array = s(array)
print(str(array_b.index(array[0])+1) + " " + str(array_b.index(array[len(array)//2])+1) + " " + str(array_b.index(array[-1])+1), file=fout)
fout.close()
