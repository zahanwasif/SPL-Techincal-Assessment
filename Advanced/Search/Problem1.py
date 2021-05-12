def findPairs(a, b):
    dic = {}
    result = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] + a[j] == b:
                result.append((a[i] , a[j]))
    return result

def filter_identical(arr):
    result = []
    for i in arr:
        if (i[0], i[1]) not in result and (i[1], i[0]) not in result:
            result.append(i)
    return result 

arr = [10, 12, 14, 16, 18]
x = findPairs(arr, 30)
print("Orignal : " , x)
print("Filtered : ", filter_identical(x))