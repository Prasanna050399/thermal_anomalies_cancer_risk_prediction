# main.py
from PyQt5.QtCore import QThread, QMutex
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
import sys
import worker

MAX = 8


class Form(QWidget):

  def __init__(self):
     super().__init__()
     self.label = QLabel("0")
     
     self.objs = list() ##
     self.threads = list() ##
     self.mutex = QMutex()

     self.setupThreads() ##

     #'''
     for thread in self.threads:
         thread.start()
     #'''

     '''
     # 1 - create Worker and Thread inside the Form
     self.obj = worker.Worker()  # no parent!
     self.thread = QThread()  # no parent!

     # 2 - Connect Worker`s Signals to Form method slots to post data.
     self.obj.intReady.connect(self.onIntReady)

     # 3 - Move the Worker object to the Thread object
     self.obj.moveToThread(self.thread)

     # 4 - Connect Worker Signals to the Thread slots
     self.obj.finished.connect(self.thread.quit)

     # 5 - Connect Thread started signal to Worker operational slot method
     self.thread.started.connect(self.obj.procCounter)

     # * - Thread finished signal will close the app if you want!
     #self.thread.finished.connect(app.exit)
     self.thread.finished.connect(self.threadEnded)

     # 6 - Start the thread
     self.thread.start()
     '''

     # 7 - Start the form
     self.initUI()


  def initUI(self):
      grid = QGridLayout()
      self.setLayout(grid)
      grid.addWidget(self.label,0,0)

      self.move(300, 150)
      self.setWindowTitle('thread test')
      self.show()

  def setupThreads(self):
      for i in range(MAX):
          obj = worker.Worker(i, self.mutex)
          thread = QThread()
          obj.intReady.connect(self.onIntReady)
          obj.finished.connect(self.threadEnded)
          obj.moveToThread(thread)
          obj.finished.connect(thread.quit)
          thread.started.connect(obj.procCounter)
          #thread.finished.connect(self.threadEnded)
          self.objs.append(obj)
          self.threads.append(thread)

  def onIntReady(self, i, j):
      res = i+j
      self.label.setText("{}".format(res))
      #print(i)
      #print("print ", res)

  def threadEnded(self, idx):
      print("thread ended function")
      print("thread ", str(idx), " execution ended successfully")
      print("done")

app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
