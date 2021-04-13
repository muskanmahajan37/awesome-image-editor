from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from awie.canvas import Canvas
from awie.toolbar import ToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Awesome Image Editor")

        tb = ToolBar()
        self.addToolBar(Qt.LeftToolBarArea, tb)

        # uncomment to disable dock widgets' splitters
        # self.setStyleSheet("QMainWindow::separator {width: 0px; border: none;}")

        self.setDockOptions(QMainWindow.AllowNestedDocks | QMainWindow.AllowTabbedDocks)

        cvs = Canvas()
        self.setCentralWidget(cvs)
