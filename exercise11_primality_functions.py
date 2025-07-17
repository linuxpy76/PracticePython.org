num = int(input("Enter a number: "))

a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
    if num > 1:
        if len(a) == 0:
            print("Prime")
        else:
            print("Composite")
    else:
        print("Composite")

is_prime(num)