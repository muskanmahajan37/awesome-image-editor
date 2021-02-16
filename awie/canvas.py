from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPixmap, QBrush, QPen, QPalette
from PyQt5.QtOpenGL import QGLFormat, QGLWidget, QGL
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsEllipseItem, QGraphicsRectItem, \
    QScrollArea, QLabel, QSizePolicy


class Canvas(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        filePath = None

        imageLabel = QLabel()
        imageLabel.setBackgroundRole(QPalette.Base)
        imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        imageLabel.setScaledContents(True)

        self.setBackgroundRole(QPalette.Dark)
        self.setWidget(imageLabel)
        self.setVisible(False)
