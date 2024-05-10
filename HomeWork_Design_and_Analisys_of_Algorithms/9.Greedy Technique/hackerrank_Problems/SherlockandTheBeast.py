# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

# summary problem
# use only 3 or 5 to construct a number with n degits
# the number of 3's it contains is devisible by 5
# the number of 5's it contains is devisible by 3



def decentNumber(n):
    constructNumber = ""
    while n > 3 and n % 3 != 0:
        n = n - 5
        constructNumber += "33333"

    if n % 3 != 0:
        print(-1)
        return
    
    numberof5 = n // 3
    while numberof5:
        constructNumber += "555"
        numberof5 -= 1

    print(constructNumber[::-1])


decentNumber(14)


    
 
    
    
