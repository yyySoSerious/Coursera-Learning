# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

def assign_jobs(n_workers, jobs):
    result = []
    n_jobs = len(jobs)
    threads = [(0, i) for i in range(n_workers)]
    heapq.heapify(threads)
    for job_idx in range(n_jobs):
        start_time, worker_id = heapq.heappop(threads)
        result.append(AssignedJob(worker_id, start_time))
        finish_time = jobs[job_idx] + start_time
        heapq.heappush(threads, (finish_time, worker_id))

    return result

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
