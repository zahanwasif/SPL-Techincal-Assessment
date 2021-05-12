string1 = "zahan"
string2 = "hussnain"

def shareSubString(a , b):
    output = 0
    for i in string1:
        if i in string2:
            output = 1
            break
    return output

print(shareSubString(string1, string2))