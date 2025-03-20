import itertools

def naive_job_sequencing(jobs):
    max_profit = 0
    best_sequence = None

    for sequence in itertools.permutations(jobs):
        slot = [False] * len(jobs)
        profit = 0
        valid_sequence = []

        for job in sequence:
            for i in range(min(len(jobs), job[1]) - 1, -1, -1):
                if not slot[i]:
                    slot[i] = True
                    profit += job[2]
                    valid_sequence.append(job)
                    break

        if profit > max_profit:
            max_profit = profit
            best_sequence = valid_sequence

    return best_sequence, max_profit

def optimized_job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = len(jobs)
    
    slot = [False] * n
    result = [None] * n

    for job in jobs:
        for i in range(min(n, job[1]) - 1, -1, -1):
            if not slot[i]:
                slot[i] = True
                result[i] = job
                break

    scheduled_jobs = [job for job in result if job is not None]
    total_profit = sum(job[2] for job in scheduled_jobs)

    return scheduled_jobs, total_profit

jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]

print('Naive Approach:', naive_job_sequencing(jobs))
print('Greedy Approach:', optimized_job_sequencing(jobs))
