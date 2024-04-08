

def expo(a, b):
    if b==1:
        return a
    
    res = expo(a,b//2)
    
    return (res*res) if( b%2== 0) else a*res*res


a = int(input("Enter the value for 'a': "))
b = int(input("Enter the value for 'b': "))

print(f"{a}^{b} =", expo(a,b))