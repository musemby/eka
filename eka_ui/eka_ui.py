#!/usr/bin/env python
from functools import partial

from PyQt4 import QtCore, QtGui

import dominus

try:
    import configdialog_rc3
except ImportError:
    import configdialog_rc2

try:
    import animatedtiles_rc3
except ImportError:
    import animatedtiles_rc2



class MasterPage(QtGui.QWidget):
    def __init__(self, parent=None, title=None):
        super(MasterPage, self).__init__(parent)

        self.title = title

        compressionGroup = QtGui.QGroupBox(self.title)

        browseFolderButton = self.createButton("&Browse...", self.browse_folder)
        browseFileButton = self.createButton("&Browse...", self.browse_file)

        processButton = self.createButton(self.title, self.process_function)

        self.directoryComboBox = self.createComboBox(QtCore.QDir.currentPath())
        self.fileComboBox = self.createComboBox(QtCore.QDir.currentPath())
        directoryLabel = QtGui.QLabel("Destination folder")
        fileLabel = QtGui.QLabel("Target file")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(compressionGroup)
        mainLayout.addStretch(1)

        compressionLayout = QtGui.QGridLayout()
        compressionLayout.setSpacing(15)
        compressionLayout.addWidget(fileLabel, 2, 0)
        compressionLayout.addWidget(self.fileComboBox, 4, 0)
        compressionLayout.addWidget(browseFileButton, 4, 1)

        compressionLayout.addWidget(directoryLabel, 6, 0)
        compressionLayout.addWidget(self.directoryComboBox, 7, 0)
        compressionLayout.addWidget(browseFolderButton, 7, 1)

        compressionLayout.addWidget(processButton, 8, 0)

        compressionGroup.setLayout(compressionLayout)
        mainLayout.addWidget(compressionGroup)

        self.setLayout(mainLayout)


    def browse_file(self):
        file = QtGui.QFileDialog.getOpenFileName(self, "Find Files",
                QtCore.QDir.currentPath())

        if file:
            self.target_file = file
            if self.fileComboBox.findText(file) == -1:
                self.fileComboBox.addItem(file)

            self.fileComboBox.setCurrentIndex(self.fileComboBox.findText(file))
        

    def browse_folder(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Find Folder",
                QtCore.QDir.currentPath())

        if directory:
            self.destination = directory
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

    def process_function(self):
        raise NotImplemented()
    
    def createComboBox(self, text=""):
        comboBox = QtGui.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        return comboBox

    def createButton(self, text, function):
        button = QtGui.QPushButton(text)
        button.clicked.connect(function)
        return button


def sleep():
    import time
    time.sleep(2)

# ======================================================================================================================
# These next 4 classes handle their respective functionalities. In the `process_function` we have access to self.target file
# and self.destination. Replace the sleep  call and print statements with the relevant code.
    

class CompressPage(MasterPage):
    def process_function(self):
        try:
            sleep()
            print(self.target_file)
            print(self.destination)
            QtGui.QMessageBox.information(
            self, "Eka", "Successfully compressed {} \n Check {} for the compressed file".format(
                self.target_file.split('/')[-1], self.destination))
        except:
            QtGui.QMessageBox.critical(self, "Eka", "An error ocurred while compressing the file. Please try again")


class DecompressPage(MasterPage):
    def process_function(self):
        try:
            sleep()
            print(self.target_file)
            print(self.destination)
            QtGui.QMessageBox.information(
            self, "Eka", "Successfully decompressed {} \n Check {} for the decompressed file".format(
                self.target_file.split('/')[-1], self.destination))
        except:
            QtGui.QMessageBox.critical(self, "Eka", "An error ocurred while decompressing the file. Please try again")


class EncryptPage(MasterPage):
    def process_function(self):
        try:
            sleep()
            print(self.target_file)
            print(self.destination)
            QtGui.QMessageBox.information(
            self, "Eka", "Successfully encrypted {} \n Check {} for the encrypted file".format(
                self.target_file.split('/')[-1], self.destination))
        except:
            QtGui.QMessageBox.critical(self, "Eka", "An error ocurred while encrypting the file. Please try again")


class DecryptPage(MasterPage):
    def process_function(self):
        try:
            sleep()
            print(self.target_file)
            print(self.destination)
            QtGui.QMessageBox.information(
            self, "Eka", "Successfully decrypted {} \n Check {} for the decrypted file".format(
                self.target_file.split('/')[-1], self.destination))
        except:
            QtGui.QMessageBox.critical(self, "Eka", "An error ocurred while decrypting the file. Please try again")


# ======================================================================================================================

class View(QtGui.QGraphicsView):
    def resizeEvent(self, event):
        super(View, self).resizeEvent(event)
        self.fitInView(self.sceneRect(), QtCore.Qt.KeepAspectRatio)


class ConfigDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(90, 78))
        self.contentsWidget.setMovement(QtGui.QListView.Static)
        self.contentsWidget.setMaximumWidth(126)
        self.contentsWidget.setSpacing(8)

        self.pagesWidget = QtGui.QStackedWidget()
        self.pagesWidget.addWidget(CompressPage(title='Compress File'))
        self.pagesWidget.addWidget(DecompressPage(title='Decompress File'))
        self.pagesWidget.addWidget(EncryptPage(title='Encrypt File'))
        self.pagesWidget.addWidget(DecryptPage(title='Decrypt File'))

        bgPix = QtGui.QPixmap(':/images/Time-For-Lunch-2.jpg')
        scene = QtGui.QGraphicsScene(-350, -350, 700, 700)
        view = View(scene)
        view.setBackgroundBrush(QtGui.QBrush(bgPix))
        view.show()

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)


        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

        self.setWindowTitle("Eka")

    def changePage(self, current, previous):
        if not current:
            current = previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    def createIcons(self):
        configButton = QtGui.QListWidgetItem(self.contentsWidget)
        configButton.setIcon(QtGui.QIcon(':/images/update.png'))
        configButton.setText("Compress")
        configButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        configButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        updateButton = QtGui.QListWidgetItem(self.contentsWidget)
        updateButton.setIcon(QtGui.QIcon(':/images/update.png'))
        updateButton.setText("Decompress")
        updateButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        updateButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        configButton = QtGui.QListWidgetItem(self.contentsWidget)
        configButton.setIcon(QtGui.QIcon(':/images/config.png'))
        configButton.setText("Encrypt")
        configButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        configButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        updateButton = QtGui.QListWidgetItem(self.contentsWidget)
        updateButton.setIcon(QtGui.QIcon(':/images/config.png'))
        updateButton.setText("Decrypt")
        updateButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        updateButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = ConfigDialog()
    sys.exit(dialog.exec_())    
