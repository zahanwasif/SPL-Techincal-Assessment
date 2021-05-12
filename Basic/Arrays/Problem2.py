from Problem1 import rotLeft
from copy import deepcopy

arr = [1,2,3,4,5]
output = []
temp = deepcopy(arr)

for i in range(len(arr)):
    temp = rotLeft(temp, len(temp) - 1)
    output.append(temp[0])
    temp.pop(0)


print("Initial array : ",arr)
print("Output array : ",output)

    
print("Yes it is done by rotLeft function. The conplexity is O(n^2) where n is the total number of integers in the array")