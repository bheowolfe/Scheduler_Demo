class Process:
    def __init__(self, duration, arrival, PID):
        self.duration = duration
        self.arrival = arrival
        self.completion = 0
        self.firstRun = 0
        self.PID = PID
        self.state = 0
        self.notStarted = True

    def run(self, time):
        if self.notStarted:
            self.firstRun = time
            self.notStarted = False
            self.state = 1
        self.duration = self.duration - 1

    def complete(self, time):
        self.completion = time


#makes Processes and puts them in a List
def createProcess():
    processes = []
    processes.append(Process(12, 0, 1234))
    processes.append(Process(2, 0, 1235))
    processes.append(Process(7, 3, 1236))
    processes.append(Process(3, 13, 1237))
    processes.append(Process(2, 16, 1238))
    #Processes in order of arrival in list
    #for i in range(5):
    #  current = Process(11-(i*2),i+1,10+i)
    #  processes.append(current)
    return processes


def runProcess(queue, time, pl):
    if (queue != []):
        queue[pl].run(time)
        #remove finished processes
        if queue[pl].duration == 0:
            queue[pl].complete(time)
            TFR = TFR + queue[pl].firstRun - queue[pl].arrival
            TTT = TTT + queue[pl].completion - queue[pl].arrival
            numComplete = numComplete + 1
            print('PID:', queue[pl].PID)
            print('Response Time:', queue[pl].firstRun - queue[pl].arrival)
            print('Turnaround Time:', queue[pl].completion - queue[pl].arrival)
            queue.pop(pl)
    return queue


def FIFO():
    processes = createProcess()
    queue = []
    time = 0
    TRT = 0
    TTT = 0
    numComplete = 0
    while processes != [] or queue != []:
        #add process to queue as they arrive
        shift = 0
        for i in range(len(processes)):
            if processes[i + shift].arrival == time:
                queue.append(processes[i + shift])
                processes.pop(i + shift)
                shift = shift - 1
        #have process run
        if (queue != []):
            queue[0].run(time)
            #remove finished processes
            if queue[0].duration == 0:
                queue[0].complete(time)
                TRT = TRT + queue[0].firstRun - queue[0].arrival
                TTT = TTT + queue[0].completion - queue[0].arrival
                numComplete = numComplete + 1
                print('PID:', queue[0].PID)
                print('Response Time:', queue[0].firstRun - queue[0].arrival)
                print('Turnaround Time:',
                      queue[0].completion - queue[0].arrival)
                queue.pop(0)
        time = time + 1
    print('Average Response Time:', TRT / numComplete)
    print('Average Turnaround Time:', TTT / numComplete)


def SJF():
    processes = createProcess()
    queue = []
    time = 0
    TRT = 0
    TTT = 0
    numComplete = 0
    while processes != [] or queue != []:
        #place process to queue as they arrive in order of duration ignoring process that is running
        shift = 0
        for i in range(len(processes)):
            if processes[i + shift].arrival == time:
                #print("Adding process",processes[i + shift].PID, 'to queue')
                if len(queue) <= 1:
                    #print('At place',len(queue))
                    queue.append(processes[i + shift])
                else:
                    done = True
                    for j in range(len(queue) - 1):
                        if processes[i + shift].duration < queue[
                                j + 1].duration and done:
                            #print('At place',j+1)
                            queue.insert(j + 1, processes[i + shift])
                            done = False
                    if done:
                        #print('At place',len(queue))
                        queue.append(processes[i + shift])
                processes.pop(i + shift)
                shift = shift - 1
        if (queue != []):
            queue[0].run(time)
            #remove finished processes
            if queue[0].duration == 0:
                queue[0].complete(time)
                TRT = TRT + queue[0].firstRun - queue[0].arrival
                TTT = TTT + queue[0].completion - queue[0].arrival
                numComplete = numComplete + 1
                print('PID:', queue[0].PID)
                print('Response Time:', queue[0].firstRun - queue[0].arrival)
                print('Turnaround Time:',
                      queue[0].completion - queue[0].arrival)
                queue.pop(0)
        time = time + 1
    print('Average Response Time:', TRT / numComplete)
    print('Average Turnaround Time:', TTT / numComplete)


def STCF():
    processes = createProcess()
    queue = []
    time = 0
    TRT = 0
    TTT = 0
    numComplete = 0
    while processes != [] or queue != []:
        #place process to queue as they arrive in order of duration
        shift = 0
        for i in range(len(processes)):
            if processes[i + shift].arrival == time:
                #print("Adding process",processes[i + shift].PID, 'to queue')
                if len(queue) <= 1:
                    #print('At place',len(queue))
                    queue.append(processes[i + shift])
                else:
                    done = True
                    for j in range(len(queue)):
                        if processes[
                                i +
                                shift].duration < queue[j].duration and done:
                            #print('At place',j)
                            queue.insert(j, processes[i + shift])
                            done = False
                    if done:
                        #print('At place',len(queue))
                        queue.append(processes[i + shift])
                processes.pop(i + shift)
                shift = shift - 1
        #have process run
        if (queue != []):
            queue[0].run(time)
            #remove finished processes
            if queue[0].duration == 0:
                queue[0].complete(time)
                TRT = TRT + queue[0].firstRun - queue[0].arrival
                TTT = TTT + queue[0].completion - queue[0].arrival
                numComplete = numComplete + 1
                print('PID:', queue[0].PID)
                print('Response Time:', queue[0].firstRun - queue[0].arrival)
                print('Turnaround Time:',
                      queue[0].completion - queue[0].arrival)
                queue.pop(0)
        time = time + 1
    print('Average Response Time:', TRT / numComplete)
    print('Average Turnaround Time:', TTT / numComplete)


def RR():
    processes = createProcess()
    queue = []
    time = 0
    TRT = 0
    TTT = 0
    numComplete = 0
    at = 0
    while processes != [] or queue != []:
        #add process to queue as they arrive
        shift = 0
        for i in range(len(processes)):
            if processes[i + shift].arrival == time:
                queue.append(processes[i + shift])
                processes.pop(i + shift)
                shift = shift - 1
        #have process run
        if (queue != []):
            queue[0].run(time)
            #remove finished processes
            if queue[0].duration == 0:
                queue[0].complete(time)
                TRT = TRT + queue[0].firstRun - queue[0].arrival
                TTT = TTT + queue[0].completion - queue[0].arrival
                numComplete = numComplete + 1
                print('PID:', queue[0].PID)
                print('Response Time:', queue[0].firstRun - queue[0].arrival)
                print('Turnaround Time:',
                      queue[0].completion - queue[0].arrival)
                queue.pop(0)
        #move along queue
        #print('at:',at,' queue length:',len(queue))
        if at + 1 >= len(queue):
            at = 0
        else:
            at = at + 1
        time = time + 1
    print('Average Response Time:', TRT / numComplete)
    print('Average Turnaround Time:', TTT / numComplete)


#STCF()
#SJF()
#FIFO()
RR()
#testing()
