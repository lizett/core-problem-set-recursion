# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n<0:
        raise ValueError("We can't do negative numbers!")
    elif n==0:
        return 1
    else:
        return factorial (n-1) * n

# reverse
def reverse (text):
    if text == "":
        return text
    return reverse(text[1:]) + text[0]

# bunny
def bunny(count):
    # base case
    if count == 0:
        return count
    return 2 + bunny(count-1)

# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False

