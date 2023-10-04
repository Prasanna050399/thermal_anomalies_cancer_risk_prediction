# worker.py
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QMutex
import time
from random import randint ##


class Worker(QObject):
    finished = pyqtSignal(int)
    intReady = pyqtSignal(int,int)

    def __init__(self, num, mutex):
        super().__init__()
        self.idx = num
        self.mutex = mutex


    @pyqtSlot()
    def procCounter(self): # A slot takes no params
        #for i in range(1, 10):
        for i in range(0, 5): ##
            time.sleep(1)
            #self.intReady.emit(i, i+1)
            num1 = randint(1, 100) ##
            num2 = randint(1, 100) ##
            self.mutex.lock()
            self.intReady.emit(num1, num2) ##
            print("thread ", self.idx, " sum ", num1+num2)
            self.mutex.unlock()
        print(self.idx, "thread job finished")
        self.finished.emit(self.idx)
        print(self.idx, "thread ended")
