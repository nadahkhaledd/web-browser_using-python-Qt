#!/usr/bin/python3

import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar, QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QImage, QWindow
from PyQt5.QtCore import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()


class App(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("web browser")
        self.createApp()
        self.setBaseSize(1366, 768)

    def createApp(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.tabBar = QTabBar(movable=True, tabsClosable=True)
        self.tabBar.tabCloseRequested.connect(self.closeTab)
        self.tabBar.addTab("tab1")
        self.tabBar.addTab("tab2")
        self.tabBar.setCurrentIndex(0)

        self.toolbar = QWidget()
        self.toolbarLayout = QHBoxLayout()
        self.addressBar = AddressBar()

        self.toolbar.setLayout(self.toolbarLayout)
        self.toolbarLayout.addWidget(self.addressBar)

        # set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tabBar)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)

        self.show()


    def closeTab(self, i):
        self.tabBar.removeTab(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())




