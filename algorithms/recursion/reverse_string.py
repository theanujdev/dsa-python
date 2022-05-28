# Given a string , we need to reverse it using recursion (and iteration)
# For example, input = "DSA Python", output = "nohtyP ASD"

# First we will implement the iterative solution
# Here we use a second string to store the reversed version. Time and Space complexity = O(n)


def iterative_reverse(string):
    reversed_string = ''
    for i in range(len(string)):
        reversed_string = reversed_string + string[len(string)-i-1]
    return reversed_string


print(iterative_reverse("DSA Python"))
# nohtyP ASD


def recursive_reverse(string):
    if len(string) == 0:
        return string
    return recursive_reverse(string[1:]) + string[0]


print(recursive_reverse("DSA Python"))
