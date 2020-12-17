#!/usr/bin/python3
#-*- coding:utf-8 -*-

#--------------------------------------------------------------------------------------------------------
# - by JPark @ KETI
# - since 2020-05-22
#--------------------------------------------------------------------------------------------------------

# Reference code : Multi threading
# https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/


# PyQt5 기반
from PyQt5.QtCore import *

#from PIL import Image, ExifTags # JPark

"""
from functools import partial
import subprocess
import shutil
import os
import time
"""

from ketiWidgetBase import KetiWidgetBase # (JPark) QWidget을 계승함. 반복적으로 사용하는 method를 추가 정의하여 자식 클래스들에게 제공

'''
from libs.gui.gui_ustr import ustr
from libs.gui.gui_utils import *
from libs.gui.gui_constants import *
'''

defaultImportDirs = ['/examples/face_samples109',
                     '/examples/face_samples4',
                     '/examples/face_samples3',
                     '/examples/face_samples1'
                    ]


class TabDetectLandmarksBase(KetiWidgetBase):
    fields = ['index', 'fpath', 'status']
    key, value, status = list(range(len(fields)))

    def __init__(self):
        super().__init__()
        self.filePath = ''
        # self.init_ui()
        self.idx = 0
        self.maxval = 1
        self.stopFlag = False

        # For loading all image under a directory
        self.mImgList = []
        self.dirname = None
        self.labelHist = []
        self.lastOpenDir = None

    def init_ui(self):
        # ------------------------------------------------
        # Layout
        # ------------------------------------------------
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)
        mainLayout.setContentsMargins(10, 10, 10, 10)
