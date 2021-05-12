from copy import deepcopy
def calMean(arr):
    newarr = deepcopy(arr)
    if len(arr) == 1:
        return arr[0]
    else:
        temp = newarr.pop(0)
        return int((temp + (calMean(newarr) * len(newarr))) /len(arr))

arr = [10, 12, 14, 16, 18]
print("The mean calculated by recursive call is : ", calMean(arr))
