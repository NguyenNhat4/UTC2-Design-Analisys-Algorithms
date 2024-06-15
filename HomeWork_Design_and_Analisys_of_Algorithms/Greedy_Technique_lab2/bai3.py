def greedy_assignment(time_matrix):
    num_workers = len(time_matrix)
    num_jobs = len(time_matrix[0])

    assigned_jobs = [-1] * num_jobs
    assigned_workers = [-1] * num_workers

    total_time = 0

    for worker in range(num_workers):
        min_time = float('inf')
        job_index = -1
        for job in range(num_jobs):
            if assigned_jobs[job] == -1 and time_matrix[worker][job] < min_time:
                min_time = time_matrix[worker][job]
                job_index = job
        assigned_jobs[job_index] = worker
        assigned_workers[worker] = job_index
        total_time += min_time

    return assigned_workers, total_time

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
    print(f"Công nhân {worker + 1} làm công việc {job + 1}")

print(f"Tổng thời gian: {total_time} giờ")
