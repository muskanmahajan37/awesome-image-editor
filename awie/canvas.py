from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene


class Canvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.NoDrag)

        scn = QGraphicsScene()

        pm1 = QPixmap(1024, 1024)
        pm1.fill(Qt.white)

        item = scn.addPixmap(pm1)
        self.setScene(scn)
        self.fitInView(scn.sceneRect(), Qt.KeepAspectRatio)

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        pDelta = e.pixelDelta()
        aDelta = e.angleDelta() / 8
        alt = int(e.modifiers()) & Qt.AltModifier
        steps = QPoint(0, 0)

        if not pDelta.isNull():
            # TODO: test this
            steps = pDelta
        elif not aDelta.isNull():
            steps = aDelta / 15

        fac = steps.x() if alt else steps.y()
        if fac > 0:
            self.scale(1.25, 1.25)
        else:
            self.scale(.8, .8)

    def keyReleaseEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_Space and not e.isAutoRepeat():
            self.setDragMode(QGraphicsView.NoDrag)

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_Space and not e.isAutoRepeat():
            self.setDragMode(QGraphicsView.ScrollHandDrag)

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        x = e.localPos().x()
        if e.localPos().x() > self.width():
            print(1)
        e.localPos().x()
        QGraphicsView.mouseMoveEvent(self, e)

