from PyQt5 import QtGui, QtWidgets, uic
import os
import danish_dictionnary

class MainWindow(QtWidgets.QMainWindow):

    """ Create the Mainwindow based on the corresponding *.ui file. """

    def __init__(self):
        # Get the path to the *.ui file
        this_dir = os.path.dirname(__file__)
        ui_file = os.path.join(this_dir, 'danish_vocabulary_GUI.ui')
        self._doubleclicked = False
        # Load it
        super(MainWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.my_dictionnary = danish_dictionnary.dictionnary()
        # self.my_dictionnary = self.my_dictionnary.load('my_dictionnary.txt')
        self.set_connections()
        self.show()

    def set_connections(self):
        self.add_word_pushButton.clicked.connect(self.add_word)
        self.save_pushButton.clicked.connect(self.save_dictionnary)
        self.load_pushButton.clicked.connect(self.load_dictionnary)
        self.next_word_pushButton.clicked.connect(self.next_word)
        self.valid_pushButton.clicked.connect(self.valid_word)

    def add_word(self):
        danishWord = self.new_word_danish_lineEdit.text()
        frenchWord = self.new_word_translation_lineEdit.text()
        self.new_word_danish_lineEdit.clear()
        self.new_word_translation_lineEdit.clear()
        if self.my_dictionnary.add_word(danishWord, frenchWord) == -1:
            print("word already in dictionnary")
        else:
            print('word added!')

    def save_dictionnary(self):
        filename = self.filename_lineEdit.text()
        self.my_dictionnary.save(filename)

    def load_dictionnary(self):
        filename = self.filename_lineEdit.text()
        self.my_dictionnary.load(filename)

    def next_word(self):
        self.revision_danish_lineEdit.setText(self.my_dictionnary.get_danish_word())
        self.revision_translation_lineEdit.clear()

    def valid_word(self):
        danishWord = self.revision_danish_lineEdit.text()
        frenchWord = self.revision_translation_lineEdit.text()
        self.my_dictionnary.check_words(danishWord, frenchWord)
        # self.revision_danish_lineEdit.setStyleSheet("color: rgb(255, 0, 0);")

    def showdialog():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(msgbtn)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    _mw = MainWindow()
    _mw.show()
    sys.exit(app.exec_())