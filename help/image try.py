from PyQt5 import QtGui, QtCore, QtWidgets
import cv2
import sys
from Image import Image

class DisplayImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DisplayImageWidget, self).__init__(parent)

        self.button = QtWidgets.QPushButton('Show picture')
        self.button.clicked.connect(self.show_image)
        self.image_frame = QtWidgets.QLabel()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.image_frame)
        self.setLayout(self.layout)

    #@QtCore.pyqtSlot()
    def show_image(self):
        self.image = cv2.imread('thermal_image.jpg')
        print("cv image done")
        #self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image = Image().imageConversion(self.image, 320, 240)
        print("Qimage done")
        #self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))
        Image().showOnWidget(self.image_frame, self.image)
        print("done")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    display_image_widget = DisplayImageWidget()
    display_image_widget.show()
    sys.exit(app.exec_())
