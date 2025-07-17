def fibonacci():
    num = int(input("How many do you want to generate for the fibonacci sequence?: "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            # print(fib)
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

print(fibonacci())