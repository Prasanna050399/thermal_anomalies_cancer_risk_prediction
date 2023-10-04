class Image:
    def __init__():
        self.width = 640
        self.height = 480
    
    def imageConversion(img, width = 640, height=480):
        print("in function")
        '''
            This function receives opencv image (in BGR format), optionally image width and height to resize, and gives QImage (QtGui.QImage) object
        '''
        from PyQt5 import QtGui, QtWidgets
        import cv2
        
        image = img.copy()
        print("copy done")
        image = cv2.resize(image, (width, height), interpolation = cv2.INTER_LANCZOS4)
        print("resize done")
        res = QtGui.QImage(image, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        print("qimage generated")
        return res
        
    def showOnWidget(widget, image):
        '''
            This function receives QLabel (QtWidgets.QLabel) and QImage (QtGui.QImage) objects and shows QImage on QLabel object
        '''
        from PyQt5 import QtGui, QtWidgets
        import cv2
        
        widget.setPixmap(QtGui.QPixmap.fromImage(image))
