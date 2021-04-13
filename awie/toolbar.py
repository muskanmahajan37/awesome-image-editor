from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction, QActionGroup, QToolBar

from typing import Union


# class Tool(QAction):
#     _ = QObject()
#     actGroup = QActionGroup(_)
#
#     def __init__(self, identifier: str, iconPath: str, tip: str, checked: bool = False, shortcut: QKeySequence, text: str, parent: Union[None, ):
#         super().__init__()
#
#         self.identifier = identifier
#         self.setCheckable(True)
#         self.setIcon(QIcon(iconPath))
#         self.setStatusTip("Foo")
#         self.setChecked(checked)
#         self.setShortcut(shortcut)
#         self.setText(text)
#         self.setParent(parent)
#         self.setActionGroup(self.actGroup)
#
#
# tools = [Tool("MOVE", "./icons/move.png", "Move selected", True),
#          Tool("PAN", "./icons/move.png", "Move selected"),
#          Tool("pan", "./icons/move.png", "Move selected")]


class ToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAllowedAreas(Qt.LeftToolBarArea | Qt.RightToolBarArea)
        # Force Vertical Orientation
        self.orientationChanged.connect(lambda _: self.setOrientation(Qt.Vertical))
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setStyleSheet("QToolBar { border: 0px }")

