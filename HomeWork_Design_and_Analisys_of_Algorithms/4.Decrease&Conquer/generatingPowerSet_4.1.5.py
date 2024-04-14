def power_set(S):
    if not S:
        return [[]] 
    else:
        head = S[0]
        tail = S[1:]
        tail_power_set = power_set(tail)
        head_power_set = [[head] + subset for subset in tail_power_set]
        return tail_power_set + head_power_set



original_set = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(power_set(original_set))

