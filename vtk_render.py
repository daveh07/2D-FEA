import csv
import os
import subprocess

import vtk
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTabWidget, QLabel, QLineEdit, QTableView, QSplitter, QFileDialog
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nodes = None
        self.setWindowTitle("VTK CAD Viewer")
        self.resize(900, 500)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a toolbar
        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.setFixedHeight(70)  # Set the fixed height of the toolbar

        # Create the button for displaying nodes
        self.display_nodes_button = QPushButton("Display Nodes")
        self.display_nodes_button.setFixedSize(50, 50)  # Set the fixed size of the button
        self.display_nodes_button.clicked.connect(self.display_nodes)
        self.toolbar.addWidget(self.display_nodes_button)

        # Create the button for meshing
        self.mesh_button = QPushButton("Mesh")
        self.mesh_button.setFixedSize(50, 50)  # Set the fixed size of the button
        self.mesh_button.clicked.connect(self.mesh_with_quad_elements)
        self.toolbar.addWidget(self.mesh_button)

        # Create a horizontal splitter to hold the VTK widget and the tab widget
        self.splitter = QSplitter()
        layout.addWidget(self.splitter)

        # Create VTK widget
        self.vtk_widget = QVTKRenderWindowInteractor()
        self.splitter.addWidget(self.vtk_widget)

        # Create a tab widget for the right-hand side
        self.tab_widget = QTabWidget()
        self.splitter.addWidget(self.tab_widget)

        # Create tab 1
        self.tab1 = QWidget()
        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.setup_tab1_ui()

        # Create tab 2
        self.tab2 = QWidget()
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.setup_tab2_ui()

        # Create tab 3
        self.tab3 = QWidget()
        self.tab_widget.addTab(self.tab3, "Tab 3")
        self.setup_tab3_ui()

        # Initialize the VTK scene
        self.init_vtk_scene()

    def init_vtk_scene(self):
        # Create a renderer, render window, and interactor
        self.renderer = vtk.vtkRenderer()
        self.render_window = self.vtk_widget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)
        self.render_window_interactor = self.vtk_widget.GetRenderWindow().GetInteractor()

        # Set background color
        self.renderer.SetBackground(1, 1, 1)  # White

        # Set camera position and focal point
        camera = self.renderer.GetActiveCamera()
        camera.SetPosition(0, 0, 20)
        camera.SetFocalPoint(0, 0, 0)

        # Set interactor style to vtkInteractorStyleTrackballCamera
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.render_window_interactor.SetInteractorStyle(style)

        # Start the interactor
        self.render_window.Render()
        self.render_window_interactor.Initialize()

    def setup_tab1_ui(self):
        # Add inputs for wall width, height, and thickness
        self.width_label = QLabel("Width:")
        self.width_input = QLineEdit()
        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit()
        self.thickness_label = QLabel("Thickness:")
        self.thickness_input = QLineEdit()

        layout = QVBoxLayout(self.tab1)
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.thickness_label)
        layout.addWidget(self.thickness_input)

        # Add a button to render the wall
        self.render_wall_button = QPushButton("Render Wall")
        self.render_wall_button.clicked.connect(self.render_wall)
        layout.addWidget(self.render_wall_button)

        # Add input for hole diameter
        self.diameter_label = QLabel("Hole Diameter:")
        self.diameter_input = QLineEdit()
        layout.addWidget(self.diameter_label)
        layout.addWidget(self.diameter_input)

        # Add button to create hole
        self.create_hole_button = QPushButton("Create Hole")
        self.create_hole_button.clicked.connect(self.create_hole)
        layout.addWidget(self.create_hole_button)

    def setup_tab2_ui(self):
        # Create table view
        self.table_view = QTableView()
        layout = QVBoxLayout(self.tab2)
        layout.addWidget(self.table_view)

        # Create table model
        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(["Node ID", "X", "Y", "Z"])
        self.table_view.setModel(self.table_model)

        # Add button to export data to CSV
        self.export_csv_button = QPushButton("Export to CSV")
        self.export_csv_button.clicked.connect(self.export_to_csv)
        layout.addWidget(self.export_csv_button)

    def setup_tab3_ui(self):
        # Add inputs for cylinder height and radius
        self.radius_label = QLabel("Radius:")
        self.radius_input = QLineEdit()
        self.cylinder_height_label = QLabel("Height:")
        self.cylinder_height_input = QLineEdit()

        layout = QVBoxLayout(self.tab3)
        layout.addWidget(self.radius_label)
        layout.addWidget(self.radius_input)
        layout.addWidget(self.cylinder_height_label)
        layout.addWidget(self.cylinder_height_input)

        # Add a button to render the cylinder
        self.render_cylinder_button = QPushButton("Render Cylinder")
        self.render_cylinder_button.clicked.connect(self.render_cylinder)
        layout.addWidget(self.render_cylinder_button)

    def export_to_csv(self):
        # Get data from table model
        data = []
        for row in range(self.table_model.rowCount()):
            row_data = []
            for column in range(self.table_model.columnCount()):
                item = self.table_model.item(row, column)
                row_data.append(item.text())
            data.append(row_data)

        # Prompt user for file name
        file_name, _ = QFileDialog.getSaveFileName(self, "Save as CSV", "", "CSV Files (*.csv)")

        if file_name:
            # Write data to CSV file
            with open(file_name, "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Node ID", "X", "Y", "Z"])  # Write header
                writer.writerows(data)

    def render_wall(self):
        # Retrieve values from input fields
        width = float(self.width_input.text())
        height = float(self.height_input.text())
        thickness = float(self.thickness_input.text())

        # Remove all existing actors
        self.renderer.RemoveAllViewProps()

        # Create and add the wall actor
        wall_actor = self.create_wall(width, height, thickness)
        self.renderer.AddActor(wall_actor)

        # Render the scene
        self.render_window.Render()

        # Update table with node information
        self.update_node_table(self.nodes)

        # Write VTK file
        self.write_vtk_file("wall.vtk")

    def render_cylinder(self):
        # Retrieve values from input fields
        radius = float(self.radius_input.text())
        height = float(self.cylinder_height_input.text())

        # Remove all existing actors
        self.renderer.RemoveAllViewProps()

        # Create and add the cylinder actor
        cylinder_actor = self.create_cylinder(radius, height)
        self.renderer.AddActor(cylinder_actor)

        # Render the scene
        self.render_window.Render()

        # Write VTK file
        self.write_vtk_file("cylinder.vtk")

    def update_node_table(self, nodes):
        # Clear existing data
        self.table_model.clear()

        # Add header labels
        self.table_model.setHorizontalHeaderLabels(["Node ID", "X", "Y", "Z"])

        # Insert data into table model
        for node in nodes:
            row = []
            for key in ["id", "x", "y", "z"]:
                item = QStandardItem(str(node[key]))
                row.append(item)
            self.table_model.appendRow(row)

    def create_wall(self, width, height, thickness):
        # Calculate coordinates of the nodes
        x_min, y_min, z_min = 0.0, 0.0, 0.0
        x_max, y_max, z_max = width, height, thickness

        # Create a cube source
        cube = vtk.vtkCubeSource()
        cube.SetBounds(x_min, x_max, y_min, y_max, z_min, z_max)

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(cube.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.8, 0.8, 0.8)  # Light gray color

        # Define nodes
        self.nodes = [
            {"id": 1, "x": x_min, "y": y_min, "z": (z_max+z_min) / 2},
            {"id": 2, "x": x_max, "y": y_min, "z": (z_max+z_min) / 2},
            {"id": 3, "x": x_max, "y": y_max, "z": (z_max+z_min) / 2},
            {"id": 4, "x": x_min, "y": y_max, "z": (z_max+z_min) / 2},
        ]

        return actor

    def create_cylinder(self, radius, height):
        # Create a cylinder source
        cylinder = vtk.vtkCylinderSource()
        cylinder.SetRadius(radius)
        cylinder.SetHeight(height)
        cylinder.SetResolution(30)

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(cylinder.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.8, 0.8, 0.8)  # Light gray color

        return actor

    def write_vtk_file(self, file_name):
        # Get the current renderer's scene
        scene = self.renderer.GetActors()

        # Create a VTK writer
        writer = vtk.vtkXMLPolyDataWriter()

        # Iterate through each actor in the scene
        for i in range(scene.GetNumberOfItems()):
            actor = scene.GetItemAsObject(i)
            poly_data = actor.GetMapper().GetInput()
            writer.SetInputData(poly_data)

            # Set the output file name
            writer.SetFileName(file_name)

            # Write the file
            writer.Write()

    def create_hole(self):
        diameter = float(self.diameter_input.text())

        # Create a circular hole in the VTK shape
        self.add_circular_hole(diameter)

        # Render the updated scene
        self.render_window.Render()

    def add_circular_hole(self, diameter):
        # Retrieve the current actor (assuming it is a wall for this example)
        current_actor = self.renderer.GetActors().GetLastActor()
        if not current_actor:
            return

        # Ensure the current actor has a mapper and input
        current_mapper = current_actor.GetMapper()
        if not current_mapper:
            return

        current_input = current_mapper.GetInput()
        if not current_input:
            return

        # Create a cylinder to subtract from the wall
        hole_cylinder = vtk.vtkCylinderSource()
        hole_cylinder.SetRadius(diameter / 2)
        hole_cylinder.SetHeight(100)  # Height should be greater than the thickness of the wall

        # Apply a transform to position the hole appropriately
        transform = vtk.vtkTransform()
        transform.Translate(current_actor.GetCenter())
        transform_filter = vtk.vtkTransformPolyDataFilter()
        transform_filter.SetInputConnection(hole_cylinder.GetOutputPort())
        transform_filter.SetTransform(transform)
        transform_filter.Update()

        # Ensure the transform filter has output
        if not transform_filter.GetOutput():
            return

        # Boolean operation to subtract the hole from the wall
        boolean_operation = vtk.vtkBooleanOperationPolyDataFilter()
        boolean_operation.SetOperationToDifference()
        boolean_operation.SetInputData(0, current_input)
        boolean_operation.SetInputData(1, transform_filter.GetOutput())
        boolean_operation.Update()

        # Ensure the boolean operation has output
        if not boolean_operation.GetOutput():
            return

        # Update the actor with the new geometry
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(boolean_operation.GetOutputPort())
        current_actor.SetMapper(mapper)

    # Inside the MainWindow class
    def mesh_with_quad_elements(self):
        # Retrieve values from input fields
        width = float(self.width_input.text())
        height = float(self.height_input.text())

        # Generate input file for Gmsh
        input_file_contents = f"""
        // Define geometry
        // Rectangle for wall
        Rectangle(1) = {{0, 0, 0, {width}, {height}, 0}};

        // Define mesh parameters
        Mesh.CharacteristicLengthMin = 0.1;
        Mesh.CharacteristicLengthMax = 1.0;

        // Define meshing algorithm
        Mesh.Algorithm = 2; // Quad meshing algorithm

        // Generate mesh
        Mesh 2;
        """

        # Write input file
        input_file_path = "mesh_input.geo"
        with open(input_file_path, "w") as f:
            f.write(input_file_contents)

        # Call Gmsh to generate mesh
        subprocess.run(["gmsh", "-2", input_file_path])

        # Remove input file
        os.remove(input_file_path)

        # Load the generated mesh
        mesh_file_path = "mesh_input.msh"
        reader = vtk.vtkGenericDataObjectReader()
        reader.SetFileName(mesh_file_path)
        reader.Update()

        # Get the output of the reader
        output = reader.GetOutput()

        # Create mapper
        mapper = vtk.vtkDataSetMapper()
        mapper.SetInputData(output)

        # Create actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # Add the actor to the renderer
        self.renderer.AddActor(actor)

        # Render the scene
        self.render_window.Render()

    def display_nodes(self):
        # Create a polydata to hold the spheres
        sphere_polydata = vtk.vtkPolyData()
        points = vtk.vtkPoints()
        for node in self.nodes:
            points.InsertNextPoint(node["x"], node["y"], node["z"])
        sphere_polydata.SetPoints(points)

        # Create spheres at each node position
        sphere_source = vtk.vtkSphereSource()
        sphere_source.SetRadius(0.012)  # Adjust the radius as needed

        # Create a glyph filter
        glyph_filter = vtk.vtkGlyph3D()
        glyph_filter.SetInputData(sphere_polydata)
        glyph_filter.SetSourceConnection(sphere_source.GetOutputPort())
        glyph_filter.Update()

        # Create mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(glyph_filter.GetOutputPort())

        # Create actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.0, 0.5, 1.0)  # Red color

        # Add the actor to the renderer
        self.renderer.AddActor(actor)

        # Render the scene
        self.render_window.Render()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
