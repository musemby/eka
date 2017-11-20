import dominus
import sys
import time

from PyQt4.QtGui import QDesktopWidget, QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QMessageBox, QDialog, QProgressBar, QMainWindow


def stub_encrypt():
    time.sleep(1)
    return True


class Compression(QMainWindow):
    
    def __init__(self):
        super(Compression, self).__init__()
        self.setGeometry(0, 0, 650, 550)
        self.centerOnScreen()
        self.prompt_target_file()


    def centerOnScreen (self):
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 
        
        
    def prompt_target_file(self):
        self.setWindowTitle('Eka Compress')

        btn = QPushButton("Choose file to compress", self)
        btn.clicked.connect(self.pick_target_file)
        btn.move(50, 50)
        btn.show()

        self.show()

    def prompt_destination(self):

        self.setWindowTitle('Eka Compress')

        btn = QPushButton("Choose the destination folder", self)
        btn.clicked.connect(self.pick_destination)
        btn.move(50, 50)
        btn.show()

        self.show()

    def pick_target_file(self):
        self.target_file = QFileDialog.getOpenFileName()
        self.prompt_destination()

    def pick_destination(self):
        self.destination = QFileDialog.getOpenFileName()
        self.compress_file(self.target_file, self.destination)

    # could have a transitional screen here showing target and destination

    def progress_bar(self):
        self.completed = 0
        self.canvas = QWidget()
        self.progress = QProgressBar(self.canvas)
        # self.progress.setGeometry()

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def compress_file(self, target_file, destination):
        # self.progress_bar()
        try:
            target = dominus.readbytes(target_file)
            compressed = dominus.compress(target)
            dominus.writebytes(destination, compressed)
            self.alert_success()
        except Exception:
            raise

    def alert_progress(self):
        QMessageBox.about(self, "Eka Compress", "Please wait while your file compresses")

    def alert_success(self):
        QMessageBox.about(self, "Eka Compress", "Successfully compressed {} \n Check {} for the compressed file".format(
            self.target_file.split('/')[-1], self.destination))

    def alert_failure(self):
        QMessageBox.about(self, "Eka Compress", "An error ocurred while compressing. Please try again")


def main():    
    app = QApplication(sys.argv)
    ex = Compression()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()