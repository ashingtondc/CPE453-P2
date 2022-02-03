import argparse


class Job:
    run_time = None
    arrival_time = None
    job_num = None

    # def __

class Scheduler:
    jobs = None
    algorithm = None
    quantum = None

    def __init__(self, filename, algorithm, quantum):
        try:
            with open(filename, "r") as jobs_file:
                lines = jobs_file.readlines()
                self.jobs = [self.line_to_tuple(line, index) for index, line in enumerate(lines)]
        except:
            print("Error opening specified file.")
            exit()

        self.algorithm = self.check_algorithm(algorithm)
        if quantum == None:
            self.quantum = 1
        else:
            self.quantum = quantum

    def __str__(self):
        return "Jobs: " + str(self.jobs) + "\nAlgorithm: " + self.algorithm  + "\nQuantum: " + str(self.quantum)

    def assign_job_number(self):
        self.jobs.sort(key=(lambda x: x[1]))
        for i in range(len(self.jobs)):
            job = self.jobs[i]
            job = list(job)
            job.append(i)





    def check_algorithm(self, algo):
        if algo == "SRTN" or algo == "RR":
            return algo
        return "FIFO"
    
    def line_to_tuple(self, line, index):
        split = line.split()
        split = [int(num) for num in split]
        split.append(index)
        return tuple(split)

    def start(self):
        if self.algorithm == "FIFO":
            self.FIFO()
        if self.algorithm == "SRTN":
            self.SRTN()
        if self.algorithm == "RR":
            self.RR()

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
    parser.add_argument('jobs_file', type=str,
                        help="path to .txt file containing list of jobs")
    parser.add_argument('-p', dest='alg', type=str, default="FIFO",
                        help='scheduling algorithm (options: STRN, FIFO, RR)')
    parser.add_argument('-q', dest='q', type=int, default=1,
                        help='time quantum (only used for RR scheduling)')
    args = parser.parse_args()
    
    scheduler = Scheduler(args.jobs_file, args.alg, args.q)
    print(scheduler)

    print("schedSim: Starting Scheduling Simulator")
    scheduler.start()
    