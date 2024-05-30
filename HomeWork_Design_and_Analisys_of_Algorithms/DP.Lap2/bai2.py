def compare_meetings(meeting1, meeting2):
    return meeting1[1] - meeting2[1]

def sap_xep_cuoc_hop(start, end):
    meetings = [(start[i], end[i]) for i in range(len(start))]
    
    sorted_meetings = sorted(meetings, key=compare_meetings)
    
    last_end_time = sorted_meetings[0][1]
    selected_meetings = [sorted_meetings[0]]
    
    for current_start, current_end in sorted_meetings[1:]:
        if current_start >= last_end_time:
            selected_meetings.append((current_start, current_end))
            last_end_time = current_end
    
    return selected_meetings

start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
result = sap_xep_cuoc_hop(start_times, end_times)
print(result) 
