def is5DigitNumber_allDegitisPrime(a):
    if a < 22222 and a > 77777:
       return False
    while a > 0 :
        last = a%10
        a//=10
        if isPrime(last) == False: 
            return False
        
    return True
    


    
def isPrime(a):
    if a <= 1:
        return False
    if a==2:
        return True
    squareRoot = int(a**(0.5)) + 1
    for i in range(2,squareRoot):
        if(a%i == 0):
            return False
        
    return True

def productDegitIsDevisible(a,q):
    product = 1
    while a > 0:
        product *= a%10
        a//=10
    return True if a%q == 0 else False

def contains_digit(n, digit):
    return str(digit) in str(n)  

def SumDegitIsDevisble(a,q):
    sum = 0
    while a > 0:
        sum += a%10
        a//=10
    return True if a%q == 0 else False

def Print_K_If_Satisfy_All_Condition(k,p,q,r):
    if is5DigitNumber_allDegitisPrime(k) and isPrime(k) and productDegitIsDevisible(k,q) and SumDegitIsDevisble(k,p) and not contains_digit(k,r):
        print(k, end= " ,")        
P = int(input("Input P:"))
Q = int(input("Input Q:"))
R = int(input("Input R:"))

def listK(P,Q,R):
    print("K are: ",end="")
    for k in range  (10000,100000):
        Print_K_If_Satisfy_All_Condition(k,P,Q,R)


listK(P,Q,R)