# import meshio
# import numpy as np
# import openseespy.opensees as ops
# import opsvis
# import vfo.vfo as vfo
# import pyvista as pv
#
# # Function to extract node coordinates and element connectivity from mesh file
# def read_mesh_file(mesh_file):
#     mesh = meshio.read(mesh_file)
#     node_coords = {node_id + 1: mesh.points[node_id] for node_id in range(len(mesh.points))}
#     element_connectivity = []
#     for cell in mesh.cells:
#         if cell.type == "triangle" or cell.type == "quad":  # Consider only 2D elements
#             element_connectivity.extend(cell.data.tolist())
#     return node_coords, element_connectivity
#
# # Define model parameters
# E = 30100.0  # Young's Modulus (MPa)
# nu = 0.2  # Poisson's Ratio
# thickness = 0.25  # Plate thickness (mm)
# thickness = thickness * 1000
#
# # Read node coordinates and element connectivity from mesh file
# node_coords, element_connectivity = read_mesh_file('rectangle.msh')
#
# # Check if any nodes were found
# if not node_coords:
#     print("Error: No nodes found in the mesh.")
#     exit()
#
# # Define model
# ops.wipe()  # Clear any existing model data
# ops.model('basic', '-ndm', 2, '-ndf', 2)
#
# # Define nodes
# for node_id, coords in node_coords.items():
#     x, y, _ = coords  # Unpack x and y coordinates
#     ops.node(node_id, x, y)
#
# # Define material
# ops.nDMaterial('ElasticIsotropic', 1, E, nu)
#
# # Define elements
# for i, element in enumerate(element_connectivity, start=1):
#     ops.element('quad', i, *[node_id + 1 for node_id in element], thickness, 'PlaneStress', 1)
#
# # Find nodes located at the ends of the plate
# min_x_coord = min(coord[0] for coord in node_coords.values())
# max_x_coord = max(coord[0] for coord in node_coords.values())
# end_nodes = [node_id for node_id, (x, _, _) in node_coords.items() if x in (min_x_coord, max_x_coord)]
#
# # Restraining the end nodes
# for node_id in end_nodes:
#     ops.fix(node_id, 1, 1, 1)
#
# # Function to apply load along the top edge
# def apply_load_top_edge():
#     # Define load pattern
#     ops.timeSeries('Linear', 1)
#     ops.pattern('Plain', 1, 1)
#
#     # Get the maximum y-coordinate
#     max_y_coord = max(coord[1] for coord in node_coords.values())
#
#     # Find nodes with maximum y-coordinate
#     top_edge_nodes = [node_id for node_id, coords in node_coords.items() if coords[1] == max_y_coord]
#
#     # Apply load to top edge nodes
#     y_load = -1500  # kN
#     y_load_to_nodes = (y_load * 5) / len(top_edge_nodes)
#
#     for node_id in top_edge_nodes:
#         ops.load(node_id, 0, y_load_to_nodes)
#
# # Function to apply normal load to the plate
# def apply_normal_load():
#     # Define load pattern
#     ops.timeSeries('Linear', 2)
#     ops.pattern('Plain', 1, 1)
#
#     # Define loads normal to the plate
#     for node_id in node_coords:
#         ops.load(node_id, 0, -5)  # Example normal load of -5 kN
#
# vfo.createODB(model="RC Wall", loadcase="Gravity")
#
# # Specify analysis components
# ops.algorithm('Linear')  #
# ops.constraints('Plain')  # Plain handler for constraints
# ops.numberer('RCM')  # Reverse Cuthill-McKee algorithm for numbering DOFs
# ops.integrator('LoadControl', 1)  # Load control integrator with a load factor of 0.1
# ops.system('ProfileSPD')  # ProfileSPD linear system of equations solver
# ops.test('NormDispIncr', 1.0e-6, 6)  # Convergence test: displacement increment norm
# ops.analysis('Static')  # Static analysis
#
# # Apply loads based on user selection
# selection = input("Enter '1' to apply load along the top edge, '2' to apply normal load: ")
# if selection == '1':
#     apply_load_top_edge()
# elif selection == '2':
#     apply_normal_load()
# else:
#     print("Invalid selection.")
#
# # Perform analysis
# ops.analyze(1)
#
# # Plot von Mises stress with mesh using PyVista
# mesh = pv.PolyData()
# mesh.points = np.array([node_coords[node_id] for node_id in range(1, len(node_coords) + 1)])
# mesh.cells = {"quad": np.array(element_connectivity)}
#
# # Plot von Mises stress with mesh using PyVista
# mesh = pv.PolyData()
# mesh.points = np.array([node_coords[node_id] for node_id in range(1, len(node_coords) + 1)])
# mesh.cells = {"quad": np.array(element_connectivity)}
#
# # Get von Mises stress
# sig_out = opsvis.sig_out_per_node("all")
# von_mises_stress = sig_out[:, 3]  # Assuming the 4th column contains von Mises stress
#
# # Add von Mises stress as point data
# mesh.point_data["von_mises_stress"] = von_mises_stress
#
# # Plot using PyVista
# plotter = pv.Plotter()
# plotter.add_mesh(mesh, scalars="von_mises_stress", cmap="coolwarm")
# plotter.show()

import subprocess
import vtk


# Function to generate mesh using Gmsh
def generate_mesh_with_gmsh(geo_file):
    subprocess.run(['gmsh', '-2', geo_file, '-o', 'rectangle.msh'])


# Function to read node coordinates and element connectivity from mesh file
def read_mesh_file(mesh_file):
    with open(mesh_file, 'r') as f:
        lines = f.readlines()

        # Find the start and end indices of the nodes section
        nodes_section_start = lines.index('$Nodes\n') + 1
        nodes_section_end = lines.index('$EndNodes\n')

        # Find the start and end indices of the elements section
        elements_section_start = lines.index('$Entities\n') + 1
        elements_section_end = lines.index('$EndEntities\n')

        # Read node coordinates
        node_coords = {}
        for line in lines[nodes_section_start: nodes_section_end]:
            parts = line.split()
            if len(parts) == 4:
                node_id = int(parts[0])
                x, y, z = map(float, parts[1:])
                node_coords[node_id] = (x, y, z)

        # Read element connectivity
        cells = []
        for line in lines[elements_section_start: elements_section_end]:
            parts = line.split()
            if len(parts) > 1:
                element_type = int(parts[0])
                num_tags = int(parts[1])
                nodes = [int(float(x)) for x in parts[2 + num_tags:]]
                if element_type == 6:  # Assuming only 2D elements (triangles or quads)
                    cells.append((element_type, nodes))

        return node_coords, cells


# Parse the rectangle.geo file and generate mesh with Gmsh
generate_mesh_with_gmsh('rectangle.geo')

# Read node coordinates and element connectivity from generated mesh file
node_coords, cells = read_mesh_file('rectangle.msh')

print("Cells:", cells)  # Print out the cells variable to debug

# Create VTK points
points = vtk.vtkPoints()
for node_id, coord in node_coords.items():
    points.InsertNextPoint(coord)

# Create VTK PolyData
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)

# Create mapper
mapper = vtk.vtkPolyDataMapper()

# Iterate over cells
cell_array = vtk.vtkCellArray()
for cell_type, cell_conn in cells:
    vtk_cell = vtk.vtkIdList()
    for node_id in cell_conn:
        vtk_cell.InsertNextId(node_id)
    cell_array.InsertNextCell(vtk_cell)
polydata.SetPolys(cell_array)
mapper.SetInputData(polydata)

# Create actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(1, 1, 1)  # White background

# Create render window
render_window = vtk.vtkRenderWindow()
render_window.SetSize(800, 600)
render_window.AddRenderer(renderer)

# Create render window interactor
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Initialize and start the event loop
render_window.Render()
render_window_interactor.Start()
