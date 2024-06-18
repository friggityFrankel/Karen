import sys
from PyQt6 import (QtCore, QtWidgets)
from PyQt6.QtWidgets import (QMainWindow, QLabel, QWidget)
from PyQt6.QtGui import (QMovie, QPixmap)

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('K.A.R.E.N.')
        self.setGeometry(10, 10, 720, 480)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.imageViewer = QLabel(self.centralwidget)
        self.imageViewer.setGeometry(QtCore.QRect(0, 0, 720, 480))
        image = QPixmap('images/Neutral.png')
        self.imageViewer.setPixmap(image)
        self.imageViewer.setScaledContents(True)
    
    def keyPressEvent(self, event):
        self.changeImage(event)
    
    def keyReleaseEvent(self, event):
        self.imageViewer.setPixmap(QPixmap('images/Neutral.png'))

    
    def changeImage(self, event):
        match event.key():
            case 49:
                movie = QMovie('images/Waveform.gif')
                self.imageViewer.setMovie(movie)
                movie.start()
            case 50:
                self.imageViewer.setPixmap(QPixmap('images/Happy.png'))
            case 51:
                self.imageViewer.setPixmap(QPixmap('images/Sad.png'))
            case 52:
                self.imageViewer.setPixmap(QPixmap('images/Mad.png'))
            case 53:
                self.imageViewer.setPixmap(QPixmap('images/Question.png'))
            case 54:
                self.imageViewer.setPixmap(QPixmap('images/Love.png'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = ApplicationWindow()
    window.show()

    sys.exit(app.exec())
