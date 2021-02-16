from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QDockWidget, QActionGroup, QLabel


class Tool(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.action = QAction()
        self.action.setCheckable(True)


class PanTool(Tool):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.action.setIcon(QIcon("./icons/pan.png"))
        self.action.setToolTip("Pan around the canvas")
        self.action.setChecked(True)


class SelectTool(Tool):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.action.setIcon(QIcon("./icons/pan.png"))
        self.action.setToolTip("Pan around the canvas")


class ToolBar(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Main Toolbar")
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        self.actGroup = QActionGroup(self)
        self.actGroup.addAction(PanTool().action)

        self.addActions(self.actGroup.actions())

    # def appendAction(self, action):
    #     self.actGroup.addAction(action)
    #     self.addAction(action)
