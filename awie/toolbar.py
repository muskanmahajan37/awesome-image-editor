from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction, QDockWidget, QActionGroup, QLabel, QToolBar


class Tool(QAction):
    def __init__(self, iconPath="", tip="", checked=False, shortcut=QKeySequence(), text="", parent=None, *args, **kwargs):
        super().__init__()

        self.setCheckable(True)
        self.setIcon(QIcon(iconPath))
        self.setStatusTip(tip)
        self.setChecked(checked)
        self.setShortcut(shortcut)
        self.setText(text)
        self.setParent(parent)


tools = [Tool("./icons/move.png", "Move selected", True)]



class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAllowedAreas(Qt.LeftToolBarArea | Qt.RightToolBarArea)
        # Force Vertical Orientation
        self.orientationChanged.connect(lambda _: self.setOrientation(Qt.Vertical))
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setStyleSheet("QToolBar { border: 0px }")

        self.actGroup = QActionGroup(self)
        self.actGroup.addAction(tools[0])

        self.addActions(self.actGroup.actions())

