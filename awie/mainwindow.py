from PyQt5.QtWidgets import QMainWindow, QToolBar, QToolButton, QAction, QActionGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class Tool(QAction):
    def __init__(self, parent):
        super().__init__(parent)

        self.setCheckable(True)


class PanTool(Tool):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon("./icons/pointer.png"))
        self.setToolTip("Pan around the canvas")


class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAllowedAreas(Qt.LeftToolBarArea | Qt.RightToolBarArea)

        self.actGroup = QActionGroup(self)

        self.tools = [PanTool(),
                      PanTool(),
                      PanTool(),
                      ]

        for tool in self.tools:
            self.actGroup.addAction(tool)
            self.addAction(tool)
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        myToolBar = ToolBar()
        self.addToolBar(Qt.LeftToolBarArea, myToolBar)
        
