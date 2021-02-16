from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from awie.canvas import Canvas
from awie.toolbar import ToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Awesome Image Editor")

        tb = ToolBar()
        self.addDockWidget(Qt.LeftDockWidgetArea, tb, Qt.Vertical)

        canvas = Canvas()
        self.setCentralWidget(canvas)
