
import threading
import random
import time

class Philosopher(threading.Thread):
    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):                                                              #thread command
        while(self.running):
            time.sleep(random.uniform(3,13))
            print( '%s is hungry' %self.name)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while (self.running):
            fork1.acquire(True)                                                 # return 0 when cannot set locked , return 1 when can
            locked = fork2.acquire(False)
            if locked:                                                          #if two forks are blocked go to dining.
                break
            fork1.release()                                                     #if impossible to block two forks, release first one
            print('%s swaps forks' %self.name)
            fork1, fork2 = fork2, fork1

            #to achieve deadlock comment three lines above - relate to fork releasing
        else:
            return

        self.dining()
        fork2.release()                                                         #release locks
        fork1.release()

    def dining(self):
        print('%s starts eating' %self.name)
        time.sleep(random.uniform(1,10))
        print('%s finishes eating and leaves to think' %self.name)


def dining_philosophers():
    forks = [threading.Lock() for n in range(5)]                                #return blocked objects
    philosopherNames = ('Ph1', 'Ph2', 'Ph3', 'Ph4', 'Ph5')

    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) \
            for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers:                                                      #start all threads
        p.start()
    time.sleep(100)
    Philosopher.running = False
    print("now we're finishing.")


dining_philosophers()


