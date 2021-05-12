def DistributeArray(arr,pivot):
    res = []
    for num in arr:
        if num < pivot:
            res.append(num)
    res.append(pivot)
    for num in arr:
        if num > pivot:
            res.append(num)
    return res

print(DistributeArray([1,-1,-2,2,-3,3,0,5],0))
print("The pivot given remains the same because for the even numbers either the given pivot number number and one other number would be the pivots. so we select the orignal pivot we have that is 0")