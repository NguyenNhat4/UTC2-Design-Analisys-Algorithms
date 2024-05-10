# source problem 
# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem

sticks = [1,2,3,4,5,10]
def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    for i in range(len(sticks) - 2):
        if sticks[i] < sticks[i+1] + sticks[i+2]:
            return [sticks[i+2], sticks[i+1],sticks[i]]
    return [-1]    
    

    


maximumPerimeterTriangle(sticks)
   

        

    