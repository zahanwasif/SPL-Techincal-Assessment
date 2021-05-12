def findAbsMin(arr):
    output = -1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and (abs(arr[i] - arr[j]) < output or output == -1):
                output = abs(arr[i] - arr[j])
    return output

arr = [10, 12, 13, 15, 10]

print(findAbsMin(arr))