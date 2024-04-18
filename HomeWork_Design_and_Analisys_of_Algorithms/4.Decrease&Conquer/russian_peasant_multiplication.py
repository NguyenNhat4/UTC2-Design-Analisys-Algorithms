def russian_peasant_multiplication(a, b):
    result = 0
    while b > 0:
        if b % 2 == 1:
            result += a
        a *= 2
        b //= 2
    return result

num1 = 26
num2 = 47
product = russian_peasant_multiplication(num1, num2)
print("The product of", num1, "and", num2, "is", product)
