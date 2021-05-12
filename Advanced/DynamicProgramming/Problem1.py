def fib(number):
    check = [0] * (number + 1)
    check[1] = 1
    fib_mem(number, check)
    return sum(check)

def fib_mem(number , check):
    if check[number] == 0 and number != 0:
        check[number] = fib_mem(number - 1 , check) + check[number - 2]
    return check[number]

number = int(input("Write the number n: "))
print(fib(number))

    

