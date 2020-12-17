import os

try:
    from PyQt5.QtGui import QPixmap, QKeySequence, QDesktopServices, QPixmapCache
    from PyQt5.QtWidgets import QPushButton, QComboBox, QCheckBox, QRadioButton
    from PyQt5.QtWidgets import QSizePolicy, QLabel, QAbstractItemView, QHeaderView, QProgressBar, QShortcut
    from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox
    from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
    from PyQt5.QtWidgets import QFileDialog
    from PyQt5.QtCore import Qt, QObject, QDir, QUrl, QThreadPool, QTimer, QFile, QFileInfo
except ImportError:
    print('[-] import error in PyQt5')

class KetiWidgetBase(QWidget):

    def __init__(self):
        super().__init__()

    def init_ui(self):
        print('todo')

    @staticmethod

    def updateComboBox(comboBox):
        if comboBox.findText(comboBox.currentText()) == -1:
            comboBox.addItem(comboBox.currentText())

    def createButton(self, text, member):
        button = QPushButton(text)
        button.clicked.connect(member)
        return button

    def setDefaultComboboxItems(self, combobox, texts):
        for text in texts:
            text = QDir.currentPath() + text
            combobox.setCurrentText(text)
            self.updateComboBox(combobox)



