x = {'a':1,'b':2,'d':3}
y = {'a':2,'b':2,'d':3}


def equality(x , y):
    if len(x) != len(y):
        return 0
    common = {k: x[k] for k in x if k in y and x[k] == y[k]}
    if common == x and common == y:
        return 1
    else:
        return 0

def calculate(x , y):
    output = []
    for i in x:
        for j in y:
            if {i:x[i]} not in output and {i:x[i]} == {j:y[j]}:
                output.append({i:x[i]})
    return len(output)

print("x : ", x)
print("y : ", y)
print("commons : ",calculate(x,y))
print("Yes we can find the number of common maps by using the equality function on each of the map seperately. The equality function has a worst case complexity of O(n) and the calculate functiion has the worst case complexity of O(n^2) which becomes a total of O(n^3)")
