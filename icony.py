import sys
from PyQt4.QtGui import QWidget, QApplication


class Compression(QWidget):
    
    def __init__(self):
        super(Compression, self).__init__()
        
        self.initialize()
        
        
    def initialize(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Eka Compress')    

        self.show()
        

def main():    
    app = QApplication(sys.argv)
    ex = Compression()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 