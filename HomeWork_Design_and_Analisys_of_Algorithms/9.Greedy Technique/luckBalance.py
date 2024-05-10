# // hackerrank problem
# // source problem
# // https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true

def luckBalance(k, contests):
    luck = 0
    contests.sort(reverse = True)
    for L,T in contests:
        if T == 0:
            luck += L
        else:
            if k > 0: 
                luck += L
                k -= 1
            else :
                luck -= L
    return luck

    




             
