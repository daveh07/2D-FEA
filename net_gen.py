import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class GraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rect_items = []
        self.grid_size = 20  # Size of the grid
        self.draw_enabled = False

    def enable_draw(self):
        self.draw_enabled = True

    def disable_draw(self):
        self.draw_enabled = False

    def draw_rectangle(self, rect):
        rect_item = QGraphicsRectItem(rect)
        self.addItem(rect_item)
        rect_item.setPen(QPen(Qt.blue, 2))
        rect_item.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        rect_item.setOpacity(0.5)
        self.rect_items.append(rect_item)

        # Draw nodes at the corners of the rectangle
        for corner in rect.normalized().corners():
            node = QGraphicsEllipseItem(QRectF(corner - QPointF(3, 3), QSizeF(6, 6)))
            node.setPen(QPen(Qt.black))
            node.setBrush(QBrush(Qt.black))
            self.addItem(node)

    def mousePressEvent(self, event):
        if self.draw_enabled and event.button() == Qt.LeftButton:
            rect = QRectF(event.scenePos(), QSizeF(0, 0))
            self.draw_rectangle(rect)

    def mouseMoveEvent(self, event):
        if self.draw_enabled and self.rect_items:
            rect = QRectF(self.rect_items[-1].rect().topLeft(), event.scenePos())
            self.rect_items[-1].setRect(rect)

    def mouseReleaseEvent(self, event):
        pass


class GraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setSceneRect(-300, -300, 600, 600)
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.RubberBandDrag)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scene = GraphicsScene()
    view = GraphicsView(scene)
    view.setWindowTitle("Rectangle Creator")

    button = QPushButton("Draw Rectangle")
    button.clicked.connect(scene.enable_draw)
    button.setCheckable(True)
    button.setChecked(False)  # By default, drawing is disabled
    button.setStyleSheet("QPushButton:checked { background-color: green; }")

    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(view)

    main_widget = QWidget()
    main_widget.setLayout(layout)
    main_widget.resize(800, 600)
    main_widget.show()

    sys.exit(app.exec())
