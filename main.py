#!/usr/bin/env python
#-*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Title     : CCTV image processing SW - JJJ 따라하기...
# Target OS : Windows, Mac, Linux
# Author    : JPark, 2020 @ Korea Electronics Technology Institute
# History   : ver.202009
#           : ver.202010
#           : ver.202011
#           : ver.202012
#------------------------------------------------------------------------------

#------------------------------------------------------
# 의존성 (Dependencies)
#------------------------------------------------------


try:
    from PyQt5.QtCore import (
        QFileInfo
    )
except ImportError:
    print('[-] import error in PyQt5')