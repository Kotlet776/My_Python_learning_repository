def func(num1, num2):
    if num1 > num2:
        return list(range(num2, num1))
    elif num1 < num2:
        return list(range(num1, num2))
    else:
        print("Wrong type of values or not enough numbers to iterate trought")

print(func(10, 2))
print(func(5, 5))
print(func(-3, -10))

