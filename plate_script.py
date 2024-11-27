import sys
import numpy as np
import meshio
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from meshpy import triangle

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.ax.set_aspect('equal', 'box')

        layout = QVBoxLayout(self.ui.PlateRenderContainer)
        layout.addWidget(self.canvas)

        # Initialize plate_geometry list
        self.plate_geometry = [0., 0., 0.]
        self.plot_plate()

        # Connect textChanged signals of line edits to corresponding slot functions
        self.ui.WidthInput.textChanged.connect(self.update_width)
        self.ui.LengthInput.textChanged.connect(self.update_length)
        self.ui.ThicknessInput.textChanged.connect(self.update_thickness)

        self.ui.MeshSizeInput.textChanged.connect(self.update_mesh_size)

        # Connect the RenderPlateBtn clicked signal to render_plate method
        self.ui.RenderPlateBtn.clicked.connect(self.plot_plate)
        self.ui.GenerateMeshBtn.clicked.connect(self.generate_mesh)

        # Connect ComboBox signal to method
        self.ui.ElementTypeInput.currentIndexChanged.connect(self.update_mesh_type)


        # Default Mesh Size
        self.mesh_size = 10

        # Initialize mesh type
        self.mesh_type = 'triangle'  # Default to triangle mesh type

        # Mesh vertices and elements
        self.mesh_vertices = None
        self.mesh_elements = None

    def update_width(self, text):
        try:
            self.plate_geometry[0] = float(text)
            print("Width Updated with: " + str(self.plate_geometry[0]))
        except ValueError:
            pass

    def update_length(self, text):
        try:
            self.plate_geometry[1] = float(text)
            print("Length Updated with: " + str(self.plate_geometry[1]))
        except ValueError:
            pass

    def update_thickness(self, text):
        try:
            self.plate_geometry[2] = float(text)
            print("Thickness Updated with: " + str(self.plate_geometry[2]))
        except ValueError:
            pass

    def update_mesh_size(self, text):
        try:
            self.mesh_size = float(text)
            print("Mesh Size Updated with: " + str(self.mesh_size))
        except ValueError:
            pass

    def update_mesh_type(self, index):
        # Implement this method to handle the change of mesh type
        if index == 0:  # Triangle mesh
            self.mesh_type = 'triangle'
        elif index == 1:  # Quad mesh
            self.mesh_type = 'quad'

    def plot_plate(self):
        width = self.plate_geometry[0]
        length = self.plate_geometry[1]

        self.ax.clear()
        self.ax.plot([0, width], [0, 0], 'k-')
        self.ax.plot([0, 0], [0, length], 'k-')
        self.ax.plot([width, width], [0, length], 'k-')
        self.ax.plot([0, width], [length, length], 'k-')

        self.ax.axis('off')
        self.ax.grid(False)

        self.canvas.draw()

    def generate_mesh(self):
        print("Generating mesh...")
        width = self.plate_geometry[0]
        length = self.plate_geometry[1]
        mesh_size = self.mesh_size

        # Clear previous mesh
        self.ax.clear()

        # Define the points of the plate
        points = [(0.0, 0.0), (width, 0.0), (width, length), (0.0, length)]

        # Create triangle mesh
        info = triangle.MeshInfo()
        info.set_points(points)
        info.set_facets([(0, 1), (1, 2), (2, 3), (3, 0)])
        mesh = triangle.build(info, max_volume=mesh_size)

        self.mesh_vertices = mesh.points
        self.mesh_elements = mesh.elements

        # Plot mesh
        for element in self.mesh_elements:
            # Plot triangle elements
            x = [self.mesh_vertices[node][0] for node in element]
            y = [self.mesh_vertices[node][1] for node in element]
            x.append(x[0])  # Close the loop
            y.append(y[0])  # Close the loop
            self.ax.plot(x, y, 'k-', linewidth=0.5)  # Black lines

            # Fill triangles with blue color
            x_tri = [self.mesh_vertices[node][0] for node in element]
            y_tri = [self.mesh_vertices[node][1] for node in element]
            self.ax.fill(x_tri, y_tri, color='blue', alpha=0.3)  # Blue fill, with some transparency

        # Set plot limits
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, length)

        # Update canvas to reflect the changes
        self.canvas.draw()
        self.export_mesh_data("mesh_file")
        print("Mesh generation complete")

    def export_mesh_data(self, filename):
        with open(filename, 'w') as file:
            # Write node coordinates
            file.write("## Node coordinates\n")
            for i, vertex in enumerate(self.mesh_vertices):
                file.write(f"node {i+1} {vertex[0]} {vertex[1]}\n")

            # Write element connectivity
            file.write("\n## Element connectivity\n")
            for i, element in enumerate(self.mesh_elements):
                file.write(f"element quad {i+1} {' '.join(str(node+1) for node in element)}\n")

            print("Mesh file generated")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

