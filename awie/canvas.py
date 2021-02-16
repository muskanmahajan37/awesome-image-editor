from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene


class Canvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        filePath = None
        self.spaceHeld = False

        # imageLabel = QLabel()
        # imageLabel.setBackgroundRole(QPalette.Base)
        # imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # imageLabel.setScaledContents(True)

        self.setBackgroundRole(QPalette.Base)
        # self.setWidget(imageLabel)
        # self.setVisible(False)

        scn = QGraphicsScene()
        scn.addEllipse(0, 0, 100, 100)

        self.setScene(scn)

    def wheelEvent(self, event: QtGui.QWheelEvent) -> None:
        pixelDelta = event.pixelDelta()
        angleDelta = event.angleDelta()

        if event.angleDelta().y() > 0:
            self.scale(1.25, 1.25)
        else:
            self.scale(.8, .8)

    # TODO: custom draging
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.spaceHeld:
            pass

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Space:
            if not self.spaceHeld:
                self.spaceHeld = True

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Space:
            if self.spaceHeld:
                self.spaceHeld = False
