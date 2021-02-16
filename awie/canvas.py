from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPixmap, QBrush, QPen
from PyQt5.QtOpenGL import QGLFormat, QGLWidget, QGL
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsEllipseItem, QGraphicsRectItem


class Canvas(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        # fmt = QGLFormat(QGL.SampleBuffers)
        # fmt.setSamples(4)
        # viewport = QGLWidget(fmt)
        # self.setViewport(viewport)

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        #self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setBackgroundBrush(QColor(40, 40, 40))
        #self.setMask()

        scene = QGraphicsScene()

        bg = QGraphicsRectItem(0.0, 0.0, 4096.0, 4096.0)
        bg.setBrush(QColor(50, 100, 255))
        scene.addItem(bg)

        el = QGraphicsEllipseItem(1024, 1024, 1024, 1024)
        el.setBrush(QColor(255, 100, 100))
        scene.addItem(el)

        self.setScene(scene)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scale(1.25, 1.25)
        else:
            self.scale(.8, .8)
