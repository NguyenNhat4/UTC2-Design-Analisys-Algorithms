import heapq

def greedy_assignment(time_matrix):
    total_time = 0
    num_tasks = len(time_matrix[0])
    num_workers = len(time_matrix)
    pq = []
    workers = [-1] * num_workers
    tasks = [-1] * num_tasks
    for i in range(num_workers):
        for j in range(num_tasks):
            heapq.heappush(pq, (time_matrix[i][j], i, j)) 
    while pq:
        time, worker,task = heapq.heappop(pq)
        if workers[worker] != -1 or tasks[task] != -1:
            continue
        tasks[task] = worker
        workers[worker] = task 
        total_time += time
    return workers, total_time

time_matrix = [
    [5, 6, 4, 7, 2],
    [5, 2, 4, 5, 1],
    [4, 5, 4, 6, 3],
    [5, 5, 3, 4, 2],
    [3, 3, 5, 2, 5]
]

assigned_workers, total_time = greedy_assignment(time_matrix)

print("Phân công công việc:")
for worker, job in enumerate(assigned_workers):
    print(f"Công nhân {worker + 1} làm công việc {job + 1} mất {time_matrix[worker][job]} giờ.")

print(f"Tổng thời gian: {total_time} giờ")
