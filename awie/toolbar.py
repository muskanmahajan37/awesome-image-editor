from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction, QDockWidget, QActionGroup, QLabel, QToolBar


class Tool(QAction):
    _ = QObject()
    actGroup = QActionGroup(_)

    def __init__(self, identifier='', iconPath="", tip="", checked=False, shortcut=QKeySequence(), text="", parent=None):
        super().__init__()

        self.identifier = identifier
        self.setCheckable(True)
        self.setIcon(QIcon(iconPath))
        self.setStatusTip("Foo")
        self.setChecked(checked)
        self.setShortcut(shortcut)
        self.setText(text)
        self.setParent(parent)
        self.setActionGroup(self.actGroup)


tools = [Tool("move", "./icons/move.png", "Move selected", True),
         Tool("pan", "./icons/move.png", "Move selected")]


class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAllowedAreas(Qt.LeftToolBarArea | Qt.RightToolBarArea)
        # Force Vertical Orientation
        self.orientationChanged.connect(lambda _: self.setOrientation(Qt.Vertical))
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setStyleSheet("QToolBar { border: 0px }")

        self.addActions(tools)

