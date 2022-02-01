import sys

class Job:
    run_time = None
    arrival_time = None
    job_num = None

    def __

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
    if len(sys.argv) < 2 or len(sys.argv) > 6:
        print("schedSim: Invalid number of arguments. Exiting.")
        exit()
    job_filename = None
    algorithm = None
    quantum = None
    try:
        for i in range(1, len(sys.argv)):
            if i == 1:
                job_filename = sys.argv[i]
            if i == 2:
                if sys.argv[i] != "-p" and sys.argv[i] != "-q":
                    raise Exception("Bad argument")
            if i == 3:
                if sys.argv[2] == "-p":
                    if algorithm is not None:
                        raise Exception("Repeated argument")
                    algorithm = sys.argv[i]
                if sys.argv[2] == "-q":
                    if quantum is not None:
                        raise Exception("Repeated argument")
                    quantum = int(sys.argv[i])
            if i == 4:
                if sys.argv[i] != "-p" and sys.argv[i] != "-q":
                    raise Exception("Bad argument")
            if i == 5:
                if sys.argv[4] == "-p":
                    if algorithm is not None:
                        raise Exception("Repeated argument")
                    algorithm = sys.argv[i]
                if sys.argv[4] == "-q":
                    if quantum is not None:
                        raise Exception("Repeated argument")
                    quantum = int(sys.argv[i])
    except:
        print("schedSim: Invalid arguments. Exiting.")
        exit()
    
    scheduler = Scheduler(job_filename, algorithm, quantum)
    print(scheduler)

    print("schedSim: Starting Scheduling Simulator")
    scheduler.start()
    