# no memoization

# def add80(n):
#     print("heavy calc")
#     return n+80


# memoization global cache

# cache = {}
# def add80(n):
#     if n in cache:
#         return cache[n]
#     print("heavy calc")
#     cache[n] = n+80
#     return cache[n]


# memoization in function
def add80():
    cache = {}

    def fn(n):
        if n in cache:
            return cache[n]
        print("heavy calc")
        cache[n] = n+80
        return cache[n]

    return fn


memo = add80()

# print(add80(5))
# print(add80(5))
print(memo(5))
print(memo(5))
