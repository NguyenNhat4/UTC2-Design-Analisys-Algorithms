def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 54
num2 = 24
gcd = euclid_gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", gcd)
