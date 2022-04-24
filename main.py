#!/usr/bin/python3

import sys
import os 
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar, QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QImage, QWindow
from PyQt5.QtCore import *

class App(QFrame):
    def __init__(self):
        self.setWindowTitle("web browser")
        self.setBaseSize(1366, 768)
        self.createApp()

        def createApp(self):
            self.layout = QVBoxLayout()
            self.tabBar = QTabBar()
            self.tabBar.addTab("tab1")
            self.tabBar.addTab("tab2")



