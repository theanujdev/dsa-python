def iterative_factorial(number):
    factorial = 1
    for i in range(2, number+1):
        factorial *= i
    return factorial


def recursive_factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * recursive_factorial(number-1)


print(iterative_factorial(0))
print(iterative_factorial(5))

print(recursive_factorial(0))
# 1

print(recursive_factorial(5))
# 120
