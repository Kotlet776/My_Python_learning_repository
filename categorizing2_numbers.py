def calcnum(min_val: int, max_val: int) -> dict:
    """
    Docstring for calcnum
    Calcnum accepts a minimal and a maximal value, both should be integers
    the numbers between (including) min_val and max_val are checked if they are even and divisible by 3 or
    if they are even or if they are divisible by 3.
    The function returns a dictionary whith the results.

    :param min_val: Description, The starting number to checl  
    :type min_val: int
    :param max_val: Description
    :type max_val: int
    :return: Description, The highest number to check
    :rtype: dict
    """
    if not type(min_val) == int or not type(max_val) == int:
        raise TypeError
    dictionary = {}
    if min_val > max_val:
        max_val, min_val = min_val, max_val
    for i in range(min_val, max_val+1):
        match i:
            case i if i % 2 == 0 and i % 3 == 0:
                dictionary[i] = "even+div3"
            case i if i % 2 == 0:
                dictionary[i] = "even"
            case i if i % 3 == 0:
                dictionary[i] = "div3"
            case _:
                dictionary[i] = "other"
    return dictionary
print(calcnum(1, 3))
print(calcnum(3, 1))
print(calcnum(0, 0))
print(calcnum("a", 3))
