def trim(string,tok):
    result = ''
    for character in string:
        if character == tok:
            continue
        result+=character
    return result

print(trim('We Are Your Technology Partners',' '))