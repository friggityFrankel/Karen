import sys
from PyQt6 import (QtCore, QtWidgets)
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget)
from PyQt6.QtGui import (QMovie, QPixmap)


class ApplicationWindow(QMainWindow):
    pressedKey = 0

    def __init__(self):
        super().__init__()

        screen = QApplication.primaryScreen().availableGeometry()

        self.setWindowTitle('K.A.R.E.N.')
        self.setGeometry(0, 0, screen.width(), screen.height())

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.imageViewer = QLabel(self.centralwidget)
        self.imageViewer.setGeometry(QtCore.QRect(0, 0, screen.width(), screen.height()))
        self.imageViewer.setScaledContents(True)
        self.changeNeutral()
    
    def keyPressEvent(self, event):
        if not event.isAutoRepeat() and self.pressedKey != event.key():
            self.pressedKey = event.key()
            self.changeImage()
        elif not event.key() == 49:
            self.changeNeutral()
    
    def keyReleaseEvent(self, event):
        if not event.isAutoRepeat() and self.pressedKey == 49:
            self.changeNeutral()

    def changeNeutral(self):
        print('Neutral')
        self.pressedKey = 0
        self.imageViewer.setPixmap(QPixmap('images/Neutral.png'))

    def changeImage(self):
        match self.pressedKey:
            case 49: # Waveform
                print('Waveform')
                self.playWaveform()
            case 50: # Maniacal augh
                print('Maniacal laugh')
                self.imageViewer.setPixmap(QPixmap('images/Maniacal.png'))
            case 51: # Eye roll
                print('Eye roll')
                self.imageViewer.setPixmap(QPixmap('images/EyeRoll.png'))
            case 52: # Angry
                print('Angry')
                self.imageViewer.setPixmap(QPixmap('images/Angry.png'))
            case 53: # Question
                print('Question')
                self.imageViewer.setPixmap(QPixmap('images/Question.png'))
            case 54: # Exclamation
                print('Exclamation')
                self.imageViewer.setPixmap(QPixmap('images/Exclamation.png'))
            case 55: # Love
                print('Love')
                self.imageViewer.setPixmap(QPixmap('images/Love.png'))
            case 56: # Music
                print('Music')
                self.imageViewer.setPixmap(QPixmap('images/Music.png'))
        
    def playWaveform(self):
        self.gif = QMovie('images/Waveform.gif')
        self.imageViewer.setMovie(self.gif)
        self.gif.start()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = ApplicationWindow()
    window.show()

    sys.exit(app.exec())
