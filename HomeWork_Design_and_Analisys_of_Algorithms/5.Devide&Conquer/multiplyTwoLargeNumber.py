
# a = 1234
# b= 3456

# a1 = 12
# a0 = 34

# b1 = 34 
# b0 = 56

# c1 =   multiplyTwoNumber(a1,b1)
# c0 =   multiplyTwoNumber(a0,b0)
# c2 =   multiplyTwoNumber(a1+a0,b1+b0) - (c1+c0)
# formular : c =  c1 * (10^(n-1))  + c2 * 10^(n//2) + c0



def multiplyTwoNumber(a,b):
    if a < 10 or b<10:
        return a*b
    
    n = max(len(str(a)),len(str(b)))
    half = n //2
    a1 = a//(10**half) #left half of a
    a0 = a%(10**half) # right half of a
    b1 = b//(10**half) #left half of a
    b0 = b%(10**half) # right half of a 
    c1 =   multiplyTwoNumber(a1,b1)
    c0 =   multiplyTwoNumber(a0,b0)
    c2 =   multiplyTwoNumber(a1+a0,b1+b0) - (c1+c0)
    return  c1*(10**(half*2)) + c2*(10**half) + c0
    


a = int(input("Type in value for a: "))
b = int(input("Type in value for b: "))

# print("a*b=",a*b)
print(f"{a} multiplied by {b} is {multiplyTwoNumber(a, b)}")