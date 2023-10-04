from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Window(QMainWindow):
    def __init__(self, gui):
        super(Window, self).__init__()
        self.gui = gui
        
        self.setGeometry(200, 200, 1200, 600)
        self.setWindowTitle("Main Window")
        
        self.init()
    
    def init(self):
        self.label = QLabel(self)
        self.label.setText("Just a label")
        self.label.move(20,50)
        
        self.button = QPushButton(self)
        self.button.setText("Just a button")
        self.button.clicked.connect(self.clicked)
        
    def clicked(self):
        self.label.setText("You just Pressed me")
        self.label.adjustSize()
        self.button.setText("You just Pressed me")
        self.button.adjustSize()

if __name__ == "__main__":
    gui = QApplication(argv)
    win = Window(gui)
    win.show()
    exit(gui.exec_())