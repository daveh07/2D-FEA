import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt

class GridWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

        # Set up the grid
        self.grid_size = 50
        self.grid_width = 10
        self.grid_height = 10
        self.drawing_mode = False  # Flag to indicate drawing mode
        self.draw_grid()

    def draw_grid(self):
        pen = QPen(Qt.black)  # Create a pen with black color
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                point = QGraphicsEllipseItem(x * self.grid_size, y * self.grid_size, 1, 1)
                point.setPen(pen)  # Set the pen for the point
                point.setFlag(QGraphicsEllipseItem.ItemIsSelectable)  # Enable selection
                self.scene.addItem(point)

    def mousePressEvent(self, event):
        if self.drawing_mode and event.button() == Qt.LeftButton:
            x = event.pos().x() // self.grid_size * self.grid_size  # Round to nearest grid intersection
            y = event.pos().y() // self.grid_size * self.grid_size
            point = QGraphicsEllipseItem(x, y, 1, 1)  # Draw a small ellipse as a point
            point.setPen(QPen(Qt.black))  # Set the pen color
            self.scene.addItem(point)

    def set_drawing_mode(self, mode):
        self.drawing_mode = mode


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid App")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.grid_widget = GridWidget()
        layout.addWidget(self.grid_widget)

        self.draw_button = QPushButton("Draw Mode")
        self.draw_button.clicked.connect(self.toggle_drawing_mode)
        layout.addWidget(self.draw_button)

    def toggle_drawing_mode(self):
        self.grid_widget.set_drawing_mode(not self.grid_widget.drawing_mode)
        if self.grid_widget.drawing_mode:
            self.draw_button.setText("Drawing Mode On")
        else:
            self.draw_button.setText("Drawing Mode Off")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
