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
                self.jobs = []
                job_num = 0
                for line in jobs_file:
                    line = line.split()
                    job = Job(int(line[0]), int(line[1]), job_num)
                    self.jobs.append(job)
        except:
            print(f"Error opening {filename}.")
            exit()

        self.algorithm = self.check_algorithm(algorithm)
        self.quantum = quantum

    def __str__(self):
        return f"Jobs: {self.jobs} \nAlgorithm: {self.algorithm} \nQuantum: {self.quantum}"

    def assign_job_number(self):
        self.jobs.sort(key=(lambda x: x[1]))
        for i in range(len(self.jobs)):
            job = self.jobs[i]
            job = list(job)
            job.append(i)

    def check_algorithm(self, alg):
        if alg == "SRTN":
            return self.SRTN 
        elif alg == "RR":
            return self.RR
        return self.FIFO

    def start(self):
        # pseudocode:
        # time = 0
        # while (jobs in job list):
        #    job = self.alg() # get next job
        #    job.execution_time += 1
        #       if job.execution_time > job.run_time:
        #       remove job from job list
        #       job waiting time = current time - execution time - run time
        # then, print the results
        pass

    def FIFO(self):
        print("schedSim: Using FIFO algorithm.")
        self.jobs.sort(key=(lambda x: x[1]))
        print(self.jobs)
    
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
    print(scheduler)
    # for job in scheduler.jobs:
    #     print(job)

    print("schedSim: Starting Scheduling Simulator")
    scheduler.start()
    