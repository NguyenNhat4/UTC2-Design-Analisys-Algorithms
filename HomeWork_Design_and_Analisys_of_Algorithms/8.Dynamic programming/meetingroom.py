def meetingRoom(s, f):
    sorted_times = sorted(zip(s, f), key=lambda x: x[1])
    count = 0
    end_time = 0
    
    for start, end in sorted_times:
        if start >= end_time:
            count += 1
            end_time = end
    
    return count
/bin/bash: line 1: q: command not found
