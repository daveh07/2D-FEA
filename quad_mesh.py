import os
import sys
import numpy as np
import meshio
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import gmsh

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
        self.mesh_type = 'quad'  # Default to quad mesh type

        # Mesh vertices and elements
        self.mesh_vertices = None
        self.mesh_elements = None

        # Connect the ToggleHoleBtn clicked signal to toggle_hole method
        self.ui.toggleHoleBtn.clicked.connect(self.toggle_hole)

        # Default hole state
        self.hole_enabled = False

    def toggle_hole(self):
        self.hole_enabled = not self.hole_enabled
        if self.hole_enabled:
            # Add code to generate the hole
            with open('rectangle.geo', 'w') as f:
                f.write(f"lc = {self.mesh_size};\n")
                f.write(f"width = {self.plate_geometry[0]};\n")
                f.write(f"length = {self.plate_geometry[1]};\n\n")
                f.write("Point(1) = {0, 0, 0, lc};\n")
                f.write("Point(2) = {width, 0, 0, lc};\n")
                f.write("Point(3) = {width, length, 0, lc};\n")
                f.write("Point(4) = {0, length, 0, lc};\n\n")
                f.write("Line(1) = {1, 2};\n")
                f.write("Line(2) = {2, 3};\n")
                f.write("Line(3) = {3, 4};\n")
                f.write("Line(4) = {4, 1};\n\n")
                f.write("Line Loop(5) = {1, 2, 3, 4};\n")
                f.write("Mesh.Algorithm = 8;\n")
                f.write("Plane Surface(6) = {5};\n")

                # Additional lines to define the hole
                f.write("\n")
                f.write("inner_width = 1.0;\n")
                f.write("inner_length = 1.0;\n\n")
                f.write("Point(5) = {(width - inner_width) / 2, (length - inner_length) / 2, 0, lc};\n")
                f.write("Point(6) = {(width + inner_width) / 2, (length - inner_length) / 2, 0, lc};\n")
                f.write("Point(7) = {(width + inner_width) / 2, (length + inner_length) / 2, 0, lc};\n")
                f.write("Point(8) = {(width - inner_width) / 2, (length + inner_length) / 2, 0, lc};\n\n")
                f.write("Line(5) = {5, 6};\n")
                f.write("Line(6) = {6, 7};\n")
                f.write("Line(7) = {7, 8};\n")
                f.write("Line(8) = {8, 5};\n\n")
                f.write("Line Loop(9) = {5, 6, 7, 8};\n")
                f.write("Plane Surface(10) = {9};\n")
                f.write("Recombine Surface {6, 10};\n")
        else:
            # Remove the hole and regenerate the geometry without it
            with open('rectangle_opening.geo', 'w') as f:
                f.write(f"lc = {self.mesh_size};\n")
                f.write(f"width = {self.plate_geometry[0]};\n")
                f.write(f"length = {self.plate_geometry[1]};\n\n")
                f.write("Point(1) = {0, 0, 0, lc};\n")
                f.write("Point(2) = {width, 0, 0, lc};\n")
                f.write("Point(3) = {width, length, 0, lc};\n")
                f.write("Point(4) = {0, length, 0, lc};\n\n")
                f.write("Line(1) = {1, 2};\n")
                f.write("Line(2) = {2, 3};\n")
                f.write("Line(3) = {3, 4};\n")
                f.write("Line(4) = {4, 1};\n\n")
                f.write("Line Loop(5) = {1, 2, 3, 4};\n")
                f.write("Mesh.Algorithm = 8;\n")
                f.write("Plane Surface(6) = {5};\n")
                f.write("Recombine Surface {6};\n")

        # Update the plate rendering
        self.plot_plate()

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

        # Create rectangle.geo file for mesh generation
        with open('rectangle.geo', 'w') as f:
            f.write(f"lc = {mesh_size};\n")
            f.write(f"width = {width};\n")
            f.write(f"length = {length};\n\n")
            f.write("Point(1) = {0, 0, 0, lc};\n")
            f.write("Point(2) = {width, 0, 0, lc};\n")
            f.write("Point(3) = {width, length, 0, lc};\n")
            f.write("Point(4) = {0, length, 0, lc};\n\n")
            f.write("Line(1) = {1, 2};\n")
            f.write("Line(2) = {2, 3};\n")
            f.write("Line(3) = {3, 4};\n")
            f.write("Line(4) = {4, 1};\n\n")
            f.write("Line Loop(5) = {1, 2, 3, 4};\n")
            f.write("Mesh.Algorithm = 8;\n")
            f.write("Plane Surface(6) = {5};\n")
            f.write("Recombine Surface {6};\n")

        # Import and mesh the geometry using Gmsh
        gmsh.initialize()
        gmsh.open('rectangle.geo')
        gmsh.option.setNumber("Mesh.CharacteristicLengthMin", mesh_size)
        gmsh.model.geo.synchronize()
        gmsh.model.mesh.generate(2)
        gmsh.write('rectangle.msh')
        gmsh.finalize()

        # Load the generated mesh
        mesh = meshio.read('rectangle.msh')

        # Extract vertices and cells from the mesh
        self.mesh_vertices = mesh.points
        self.mesh_elements = None
        for cell_block in mesh.cells:
            if cell_block.type == 'quad':
                self.mesh_elements = cell_block.data
                break
        if self.mesh_elements is None:
            for cell_block in mesh.cells:
                if cell_block.type == 'triangle':
                    self.mesh_elements = cell_block.data
                    break
        if self.mesh_elements is None:
            raise ValueError("No quadrilateral or triangular cells found in the mesh.")

        # Plot mesh
        for element in self.mesh_elements:
            if len(element) == 4:  # Quad element
                x = [self.mesh_vertices[node][0] for node in element]
                y = [self.mesh_vertices[node][1] for node in element]
                x.append(x[0])  # Close the loop
                y.append(y[0])  # Close the loop
                self.ax.plot(x, y, 'k-', linewidth=0.5)  # Black lines

                # Fill quads with blue color
                x_quad = [self.mesh_vertices[node][0] for node in element]
                y_quad = [self.mesh_vertices[node][1] for node in element]
                self.ax.fill(x_quad, y_quad, color='blue', alpha=0.3)  # Blue fill, with some transparency
            elif len(element) == 3:  # Triangle element
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

        # Optionally, clean up the intermediate .geo and .msh files
        # os.remove('rectangle.geo')
        # os.remove('rectangle.msh')

        print("Mesh generation complete")

    def export_mesh_data(self, filename):
        with open(filename, 'w') as file:
            # Write node coordinates
            file.write("## Node coordinates\n")
            for i, vertex in enumerate(self.mesh_vertices):
                file.write(f"node {i + 1} {vertex[0]} {vertex[1]} {vertex[2]}\n")

            # Write element connectivity
            file.write("\n## Element connectivity\n")
            for i, element in enumerate(self.mesh_elements):
                if len(element) == 4:
                    file.write(f"element quad4 {i + 1} {' '.join(str(node) for node in element)}\n")
                else:
                    raise ValueError("Elements with more than four nodes are not supported.")

        print("Mesh file generated")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())