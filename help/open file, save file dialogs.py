import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button1 = QPushButton('Open file')
        self.button1.clicked.connect(self.openFileNameDialog)
        self.button2 = QPushButton('Save file')
        self.button2.clicked.connect(self.saveFileDialog)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py);;JPG Files (*.jpg)", options=options)
        if fileName:
            print(fileName)
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        import os
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        #fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","PDF Files (*.pdf)", options=options)
        filepath = ""
        if fileName:
            print("save as ->", fileName)
            '''
            curWord = ""
            for char in fileName:
                if char == "/" or char == "\\":
                    filepath = filepath + curWord + char
                    curWord = ""
                else:
                    curWord = curWord + char
            filepath = filepath + curWord
            '''
            filepath = fileName
        else:
            print("save as no ->", desktop)
            #filepath = desktop
            for char in desktop:
                if char == "\\":
                    filepath = filepath + "/"
                else:
                    filepath = filepath + char
            filepath = filepath + "/report.pdf"
        print("final ->", filepath)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


##import os
##
##desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
##
### Prints: C:\Users\sdkca\Desktop
##print("The Desktop path is: " + desktop)
