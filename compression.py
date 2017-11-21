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
        self.setGeometry(0, 0, 450, 350)
        self.centerOnScreen()
        self.show()
        btn_compress = QPushButton("Compress", self)
        btn_compress.move(100, 100)
        btn_compress.clicked.connect(self.pick_compress_target_file)
        btn_compress.show()

        btn_decompress = QPushButton("Decompress", self)
        btn_decompress.move(250, 100)
        btn_decompress.clicked.connect(self.pick_decompress_target_file)
        btn_decompress.show()

        btn_encrypt = QPushButton("Encrypt", self)
        btn_encrypt.move(100, 200)
        btn_encrypt.clicked.connect(self.pick_encrypt_target_file)
        btn_encrypt.show()

        btn_decrypt = QPushButton("Decrypt", self)
        btn_decrypt.move(250, 200)
        btn_decrypt.clicked.connect(self.pick_decrypt_target_file)
        btn_decrypt.show()
        # self.prompt_target_file()


    def centerOnScreen (self):
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2)) 

    def pick_compress_target_file(self):
        self.compress_target_file = QFileDialog.getOpenFileName(self, "Pick a file to compress")
        self.pick_compress_destination()

    def pick_compress_destination(self):
        self.compress_destination = QFileDialog. getExistingDirectory (self, "Pick a destination for your compressed file")
        self.compress_file(self.compress_target_file, self.compress_destination)

    def pick_decompress_target_file(self):
        self.decompress_target_file = QFileDialog.getOpenFileName(self, "Pick a file to decompress")
        self.pick_decompress_destination()

    def pick_decompress_destination(self):
        self.decompress_destination = QFileDialog. getExistingDirectory (self, "Pick a destination for your decompressed file")
        self.decompress_file(self.decompress_target_file, self.decompress_destination)

    def pick_encrypt_target_file(self):
        self.encrypt_target_file = QFileDialog.getOpenFileName(self, "Pick a file to encrypt")
        self.pick_encrypt_destination()

    def pick_encrypt_destination(self):
        self.encrypt_destination = QFileDialog. getExistingDirectory (self, "Pick a destination for your encrypted file")
        self.encrypt_file(self.encrypt_target_file, self.encrypt_destination)

    def pick_decrypt_target_file(self):
        self.decrypt_target_file = QFileDialog.getOpenFileName(self, "Pick a file to decrypt")
        self.pick_decrypt_destination()

    def pick_decrypt_destination(self):
        self.decrypt_destination = QFileDialog. getExistingDirectory (self, "Pick a destination for your decrypted file")
        self.decrypt_file(self.decrypt_target_file, self.decrypt_destination)

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
            self.alert_compress_success()
        except Exception:
            raise

    def decompress_file(self, target_file, destination):
        # self.progress_bar()
        try:
            target = dominus.readbytes(target_file)
            compressed = dominus.compress(target)
            dominus.writebytes(destination, compressed)

            infile = dominus.readbytes(target_file)
            uncompressed = dominus.decompress(infile)
            outfile = open(destination + '/out.uncompressed','w')
            for bt in uncompressed:
                outfile.write(bt)
            self.alert_decompress_success()
        except Exception:
            raise

    def encrypt_file(self, target_file, destination):
        # self.progress_bar()
        try:
            target = dominus.readbytes(target_file)
            compressed = dominus.compress(target)
            dominus.writebytes(destination, compressed)
            self.alert_encrypt_success()
        except Exception:
            raise

    def decrypt_file(self, target_file, destination):
        # self.progress_bar()
        try:
            target = dominus.readbytes(target_file)
            compressed = dominus.compress(target)
            dominus.writebytes(destination, compressed)

            infile = dominus.readbytes(target_file)
            uncompressed = dominus.decompress(infile)
            outfile = open(destination + '/out.uncompressed','w')
            for bt in uncompressed:
                outfile.write(bt)
            self.alert_decrypt_success()
        except Exception:
            raise

    def alert_progress(self):
        QMessageBox.about(self, "Eka Compress", "Please wait while your file compresses")

    def alert_compress_success(self):
        QMessageBox.about(self, "Eka Compress", "Successfully compressed {} \n Check {} for the compressed file".format(
            self.compress_target_file.split('/')[-1], self.compress_destination))

    def alert_decompress_success(self):
        QMessageBox.about(self, "Eka Compress", "Successfully decompressed {} \n Check {} for the decompressed file".format(
            self.decompress_target_file.split('/')[-1], self.decompress_destination))

    def alert_encrypt_success(self):
        QMessageBox.about(self, "Eka Compress", "Successfully encrypted {} \n Check {} for the encrypted file".format(
            self.encrypt_target_file.split('/')[-1], self.encrypt_destination))

    def alert_decrypt_success(self):
        QMessageBox.about(self, "Eka Compress", "Successfully decrypted {} \n Check {} for the decrypted file".format(
            self.decrypt_target_file.split('/')[-1], self.decompress_destination))

    def alert_failure(self):
        QMessageBox.about(self, "Eka Compress", "An error ocurred while processing. Please try again")


def main():    
    app = QApplication(sys.argv)
    ex = Compression()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()