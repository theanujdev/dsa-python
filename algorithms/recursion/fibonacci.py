# Given a number, we have to return the number at that index of the fibonacci sequence.
# Fibonacci Sequence - 0 1 1 2 3 5 8 13 21 34 55 89 144 . . . .

def iterative_fibonacci(index):
    if index < 2:
        return index
    a = 0
    b = 1
    ans = 1
    for _ in range(1, index):
        ans = a + b
        a = b
        b = ans
    return ans


print(iterative_fibonacci(0))  # 0
print(iterative_fibonacci(1))  # 1
print(iterative_fibonacci(5))  # 5


def recursive_fibonacci(index):
    if index < 2:
        return index
    return recursive_fibonacci(index-1) + recursive_fibonacci(index-2)


print(recursive_fibonacci(0))  # 0
print(recursive_fibonacci(1))  # 1
print(recursive_fibonacci(5))  # 5
