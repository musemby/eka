# app = QApplication(sys.argv)
# button = QPushButton("Choose file", None)
# button.show()

# def select_file():
#     x = QFileDialog.getOpenFileName()
#     print(x)

# button.clicked.connect(select_file)
# app.exec_()


import sys
from PyQt4.QtGui import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit


class Compression(QWidget):
    
    def __init__(self):
        super(Compression, self).__init__()
        
        self.prompt_target_file()
        
        
    def prompt_target_file(self):
        
        self.setGeometry(600, 600, 500, 300)
        self.setWindowTitle('Eka Compress')

        btn = QPushButton("Choose file to compress", self)
        btn.clicked.connect(self.pick_target_file)
        btn.move(50, 50)
        btn.show()

        self.show()

    def prompt_destination(self):
        
        self.setGeometry(600, 600, 500, 300)
        self.setWindowTitle('Eka Compress')

        btn = QPushButton("Choose the destination folder", self)
        btn.clicked.connect(self.pick_destination)
        btn.move(50, 50)
        btn.show()

        self.show()

    def pick_target_file(self):
        self.to_compress = QFileDialog.getOpenFileName()
        self.prompt_destination()


    def pick_destination(self):
        self.destination = QFileDialog.getExistingDirectory()
        
        

def main():    
    app = QApplication(sys.argv)
    ex = Compression()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 