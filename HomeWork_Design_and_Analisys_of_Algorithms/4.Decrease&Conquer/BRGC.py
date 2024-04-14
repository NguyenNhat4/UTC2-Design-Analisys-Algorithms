# Generates recursively the binary reﬂected Gray code of order n
# Input: A positive integer n
# Output: A list of all bit strings of length n composing the Gray code


def BRGC(n):
    if n == 1:
        return ['0', '1']
    else:
        L1 = BRGC(n - 1)
        L2 = L1[::-1] # reverse of L1
        L1 = ['0' + bit_string for bit_string in L1]
        L2 = ['1' + bit_string for bit_string in L2]
        L = L1 + L2
        return L

# Example usage:
n = 3
gray_code = BRGC(n)
for code in gray_code:
    print(code)



# output 

# 000
# 001
# 011
# 010
# 110
# 111
# 101
# 100
