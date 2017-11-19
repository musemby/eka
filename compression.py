# app = QApplication(sys.argv)
# button = QPushButton("Choose file", None)
# button.show()

# def select_file():
#     x = QFileDialog.getOpenFileName()
#     print(x)

# button.clicked.connect(select_file)
# app.exec_()


import sys
import time

from PyQt4.QtGui import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QMessageBox, QDialog


def stub_encrypt():
    time.sleep(2)
    return True


class Compression(QDialog):
    
    def __init__(self):
        super(Compression, self).__init__()
        
        self.prompt_target_file()
        
        
    def prompt_target_file(self):
        
        # self.setGeometry(600, 600, 500, 300)
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
        self.destination = QFileDialog.getExistingDirectory()
        self.compress_file(self.target_file, self.destination)

    # could have a transitional screen here showing target and destination

    def compress_file(self, target_file, destination):
        try:
            stub_encrypt()
            self.alert_success()
        except Exception:
            self.alert_failure()

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