import argparse
from pathlib import Path

class Job:

    def __init__(self, run_time, arrival_time, job_num):
        self.run_time = run_time
        self.arrival_time = arrival_time
        self.job_num = job_num
        self.execution_time = 0 # how long this job has been running for
        self.wait_time = 0
       

    def __str__(self):
        return (f"Job Number: {self.job_num}\n"
                f"  Arrival time: {self.arrival_time}\n  Run time: {self.run_time}\n  Execution time: {self.execution_time}")


class Scheduler:
    def __init__(self, filename, algorithm = "FIFO", quantum = 1):
        try:
            with open(filename, "r") as jobs_file:
                self.ready_jobs = []
                lines = jobs_file.readlines()
                # sort jobs by arrival time and assign job times
                lines = [line.split() for line in lines]
                lines.sort(key = lambda line: line[1])
                for index, job in enumerate(lines):
                    self.ready_jobs.append(Job(int(job[0]), int(job[1]), index))
        except FileNotFoundError as e:
            print(f"Error opening {filename}.")
            exit()

        self.algorithm = self.check_algorithm(algorithm)
        self.quantum = quantum
        self.running_jobs = []
        self.finished_jobs = []


    def __str__(self):
        return f"Jobs: {self.ready_jobs} \nAlgorithm: {self.algorithm} \nQuantum: {self.quantum}"


    def check_algorithm(self, alg):
        if alg == "SRTN":
            return self.SRTN 
        elif alg == "RR":
            return self.RR
        return self.FIFO


    def start(self):
        # pseudocode:
        time = 0
        while len(self.ready_jobs) > 0 or len(self.running_jobs) > 0:
            # see if any jobs need to be scheduled
            while len(self.ready_jobs) > 0 and self.ready_jobs[0].arrival_time <= time:
                self.running_jobs.append(self.ready_jobs.pop(0))
            # see if there is a job to be run
            job_index = self.algorithm()
            if job_index >= 0: 
                job = self.running_jobs[job_index]
                # see if this job has completed
                if job.execution_time >= job.run_time:
                    self.finished_jobs.append(self.running_jobs.pop(job_index))
                    job.waiting_time = time - job.execution_time - job.arrival_time
                # if not, execute it for one unit of time
                else:
                    job.execution_time += 1            
            time += 1

        self.print_results()


    def print_results(self):
        avg_wait = 0
        avg_turnaround = 0

        for job in self.finished_jobs:
            avg_wait += job.waiting_time
            turnaround = job.waiting_time + job.execution_time
            avg_turnaround += turnaround
            print(f"Job {job.job_num} -- Turnaround {turnaround} Wait {job.waiting_time}")

        avg_wait = float(avg_wait) / len(self.finished_jobs)
        avg_turnaround = float(avg_turnaround) / len(self.finished_jobs)
        print(f"Average -- Turnaround {avg_turnaround:3.2f} Wait {avg_wait:3.2f}")


    def FIFO(self):
        # return first job if it exists, otherwise -1
        # this works because jobs were added to running_jobs in order of arrival time
        if len(self.running_jobs) > 0:
            return 0
        return -1
    

    def SRTN(self):
        pass


    def RR(self):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Scheduling simulator for CPE 453 Lab 2'
    )
    parser.add_argument('jobs_file', type=Path,
                        help="path to .txt file containing list of jobs")
    parser.add_argument('-p', dest='alg', type=str, default="FIFO",
                        help='scheduling algorithm (options: STRN, FIFO, RR)')
    parser.add_argument('-q', dest='q', type=int, default=1,
                        help='time quantum (only used for RR scheduling)')
    args = parser.parse_args()
    
    scheduler = Scheduler(args.jobs_file, args.alg, args.q)
    # print(scheduler)
    # for job in scheduler.ready_jobs:
    #     print(job)

    print("schedSim: Starting Scheduling Simulator")
    scheduler.start()
    