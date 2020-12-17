import sys
from PyQt5.QtWidgets import *

"""
fields = ['index', 'fpath', 'status']

key, value, status = list(range( len(fields) )) # JPark
print(list(range( len(fields) )))
print(key, value, status)
"""

"""
class   JJJTestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setGeometry(1000,200,300,100)

        self.pushButton1 = QPushButton("Button1")
        self.pushButton2= QPushButton("Button2")
        self.pushButton3= QPushButton("Button3")


        layout = QHBoxLayout()
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.pushButton3)

        self.setLayout(layout)
"""
class TabDetectLandmarksBase(QWidget):
    fields = ['index', 'fpath', 'status']
    key, value, status = list(range(len(fields)))

    """
    
    ''' 각종 변수들 초기값을 Init 하여 Instance 함 '''
    def __init__(self):
        super().__init__()
        self.filePath = ''
        self.init_ui()


        self.idx = 0
        self.maxval = 1
        self.stopFlag = False

        # For loading all image under a directory
        self.mImgList = []
        self.dirname = None
        self.labelHist = []
        self.lastOpenDir = None


    def init_ui(self):
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)
        mainLayout.setContentsMargins(10, 10, 10, 10)

        ''' TODO
        leftGroupBox = QGroupBox("Options")
        leftLayout = QVBoxLayout()
        '''


        '''
            그룹 박스는 상단 타이틀과 단축키 (shortcut)를 제공하며, 그 안에 다양한 위젯들을 나타낼 수 있습니다
        '''

        middleGroupBox = QGroupBox("Occulution LandMark Pages")
        middleLayout = QGridLayout()

        ''' TODO
        rightGroupBox = QGroupBox("Results")
        rightLayout = QVBoxLayout()
        '''

        ''' TODO
        mainLayout.addWidget(leftGroupBox)
        '''

        mainLayout.addWidget(middleGroupBox)

        ''' TODO
        mainLayout.addWidget(rightGroupBox)
        '''

        # ------------------------------------------------
        # Left
        # ------------------------------------------------

        ''' TODO
                self.l = QLabel("Start")
                list = ["Method01", "ETC1", "ETC2", "ETC3"]
                combobox1 = QComboBox()
                combobox1.addItems(list)

                checkbox1 =QCheckBox("옵션 1")
                checkbox2 =QCheckBox("옵션 2")
                checkbox3 =QCheckBox("옵션 3")
                checkbox4 =QCheckBox("옵션 4")
                checkbox5 =QCheckBox("옵션 5")
                #btnFileOpen = QPushButton("FileOpen")
                #btnFileOpen.clicked.connect(self.openFile)
                leftLayout.addWidget(self.l)
                leftLayout.addWidget(combobox1)
                leftLayout.addWidget(checkbox1)
                leftLayout.addWidget(checkbox2)
                leftLayout.addWidget(checkbox3)
                leftLayout.addWidget(checkbox4)
                leftLayout.addWidget(checkbox5)
                #leftLayout.addWidget(btnFileOpen)

                # Layout
                leftGroupBox.setLayout(leftLayout)
                '''

        # ------------------------------------------------
        # Middle
        # ------------------------------------------------

        middleLayout.setContentsMargins(5, 5, 5, 5)
        # self.comboboxSetF




"""

if __name__ == "__main__":
    app=QApplication(sys.argv)
    testWindows = TabDetectLandmarksBase()
    testWindows.show()
    app.exec()








