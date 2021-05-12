import copy

def rotLeft(initial, rotations):
    output = copy.deepcopy(initial)
    for i in range(rotations):
        temp = output[0]
        output.pop(0)
        output.append(temp)
    return output

def main():
    array = [1, 2, 3, 4, 5]
    print(rotLeft(array, 3))

if __name__ == "__main__":
    main()





        

    