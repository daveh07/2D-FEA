import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt
import vtkmodules.all as vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class VTKWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.renderer = vtk.vtkRenderer()
        self.render_window = vtk.vtkGenericOpenGLRenderWindow()
        self.render_window_interactor = QVTKRenderWindowInteractor(parent=self)

        self.render_window.SetInteractor(self.render_window_interactor)
        self.render_window_interactor.SetRenderWindow(self.render_window)

        self.renderer.SetBackground(0.2, 0.3, 0.4)
        self.render_window.AddRenderer(self.renderer)

        self.vtk_widget = self.render_window_interactor
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.vtk_widget)

    def set_shape(self, shape_actor):
        self.renderer.RemoveAllViewProps()
        self.renderer.AddActor(shape_actor)
        self.renderer.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()

    def resizeEvent(self, event):
        self.render_window.SetSize(self.width(), self.height())
        self.render_window_interactor.Render()
        super().resizeEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VTK Shapes Renderer")

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.vtk_widget = VTKWidget()

        self.rectangle_button = QPushButton("Rectangle")
        self.rectangle_button.clicked.connect(self.show_rectangle)

        self.width_label = QLabel("Width:")
        self.width_input = QLineEdit()
        self.width_input.setText("1")

        self.length_label = QLabel("Length:")
        self.length_input = QLineEdit()
        self.length_input.setText("1")

        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit()
        self.height_input.setText("1")

        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.draw_shape)

        toolbar_layout = QVBoxLayout()
        toolbar_layout.addWidget(self.rectangle_button)
        toolbar_layout.addWidget(self.width_label)
        toolbar_layout.addWidget(self.width_input)
        toolbar_layout.addWidget(self.length_label)
        toolbar_layout.addWidget(self.length_input)
        toolbar_layout.addWidget(self.height_label)
        toolbar_layout.addWidget(self.height_input)
        toolbar_layout.addWidget(self.draw_button)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addLayout(toolbar_layout)
        main_layout.addWidget(self.vtk_widget)

    def show_rectangle(self):
        rectangle_source = vtk.vtkCubeSource()
        rectangle_source.SetXLength(1)
        rectangle_source.SetYLength(1)
        rectangle_source.SetZLength(1)
        shape_mapper = vtk.vtkPolyDataMapper()
        shape_mapper.SetInputConnection(rectangle_source.GetOutputPort())
        shape_actor = vtk.vtkActor()
        shape_actor.SetMapper(shape_mapper)
        self.vtk_widget.set_shape(shape_actor)

    def draw_shape(self):
        width = float(self.width_input.text())
        length = float(self.length_input.text())
        height = float(self.height_input.text())

        cube_source = vtk.vtkCubeSource()
        cube_source.SetXLength(width)
        cube_source.SetYLength(length)
        cube_source.SetZLength(height)
        shape_mapper = vtk.vtkPolyDataMapper()
        shape_mapper.SetInputConnection(cube_source.GetOutputPort())
        shape_actor = vtk.vtkActor()
        shape_actor.SetMapper(shape_mapper)
        self.vtk_widget.set_shape(shape_actor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
