import meshio
import numpy as np
import openseespy.opensees as ops
import opsvis
import vfo.vfo as vfo
from matplotlib import pyplot as plt


# Function to extract node coordinates and element connectivity from mesh file
def read_mesh_file(mesh_file):
    mesh = meshio.read(mesh_file)
    node_coords = {node_id + 1: mesh.points[node_id] for node_id in range(len(mesh.points))}
    element_connectivity = []
    for cell in mesh.cells:
        if cell.type == "triangle" or cell.type == "quad":  # Consider only 2D elements
            element_connectivity.extend(cell.data.tolist())
    return node_coords, element_connectivity


# Define model parameters
E = 30100.0  # Young's Modulus (MPa)
nu = 0.2  # Poisson's Ratio
thickness = 0.35  # Plate thickness (mm)
thickness = thickness * 1000  # (Conver to m)

# Read node coordinates and element connectivity from mesh file
node_coords, element_connectivity = read_mesh_file('rectangle.msh')

# Check if any nodes were found
if not node_coords:
    print("Error: No nodes found in the mesh.")
    exit()

# Define model
ops.wipe()  # Clear any existing model data
ops.model('basic', '-ndm', 2, '-ndf', 2)

# Define nodes
for node_id, coords in node_coords.items():
    x, y, _ = coords  # Unpack x and y coordinates
    ops.node(node_id, x, y)

# Define material
ops.nDMaterial('ElasticIsotropic', 1, E, nu)

# Define elements
for i, element in enumerate(element_connectivity, start=1):
    ops.element('quad', i, *[node_id + 1 for node_id in element], thickness, 'PlaneStress', 1)

# Find nodes located at the ends of the plate
min_x_coord = min(coord[0] for coord in node_coords.values())
max_x_coord = max(coord[0] for coord in node_coords.values())
end_nodes = [node_id for node_id, (x, _, _) in node_coords.items() if x in (min_x_coord, max_x_coord)]

# Restraining the end nodes
for node_id in end_nodes:
    ops.fix(node_id, 1, 1, 1)


# Function to apply load along the top edge
def apply_load_top_edge():
    # Define load pattern
    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1)

    # Get the maximum y-coordinate
    max_y_coord = max(coord[1] for coord in node_coords.values())

    # Find nodes with maximum y-coordinate
    top_edge_nodes = [node_id for node_id, coords in node_coords.items() if coords[1] == max_y_coord]

    # Apply load to top edge nodes
    y_load = -2500  # kN
    y_load_to_nodes = (y_load * 5) / len(top_edge_nodes)
    for node in top_edge_nodes:
        ops.load(node, 0, y_load_to_nodes)


# Function to apply normal load to the plate
def apply_normal_load():
    # Define load pattern
    ops.timeSeries('Linear', 2)
    ops.pattern('Plain', 1, 1)

    # Define loads normal to the plate
    for node_id in node_coords:
        ops.load(node_id, 0, -5)  # Example normal load of -5 kN


# Specify analysis components
ops.algorithm('Newton')  # Newton's method for equilibrium iterations
ops.constraints('Plain')  # Plain handler for constraints
ops.numberer('RCM')  # Reverse Cuthill-McKee algorithm for numbering DOFs
ops.integrator('LoadControl', 1)  # Load control integrator with a load factor of 0.1
ops.system('ProfileSPD')  # ProfileSPD linear system of equations solver
ops.test('NormDispIncr', 1.0e-6, 6)  # Convergence test: displacement increment norm
ops.analysis('Static')  # Static analysis

# Apply loads based on user selection
selection = input("Enter '1' to apply load along the top edge, '2' to apply normal load: ")
if selection == '1':
    apply_load_top_edge()
elif selection == '2':
    apply_normal_load()
else:
    print("Invalid selection.")

# Perform analysis
ops.analyze(1)

# Visualization
opsvis.plot_model()
opsvis.plot_loads_2d()
plt.figure()

# Plot von Mises stress without mesh edges
sig_out = opsvis.sig_out_per_node("all")
j, jstr = 3, 'vmis'
nds_val = sig_out[:, j]
min_val = np.min(nds_val)
max_val = np.max(nds_val)
plt.title(f"{jstr}, Min: {min_val:.2f}, Max: {max_val:.2f}")
opsvis.plot_stress_2d(nds_val)  # Hide mesh edges
plt.box(False)

# Show plot
plt.show()

# Plot deformation
opsvis.plot_defo(unDefoFlag=1)
plt.axis('equal')
plt.box(False)
plt.show()
