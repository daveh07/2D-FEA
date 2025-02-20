import mplcursors
import numpy as np
import openseespy.opensees as ops
import opsvis
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Function to extract node coordinates and element connectivity from mesh file
def read_mesh_file(mesh_file):
    with open(mesh_file, 'r') as file:
        lines = file.readlines()

    node_coords = {}
    element_connectivity = []

    for line in lines:
        if line.startswith('node'):
            _, node_id, x, y = line.split()
            node_coords[int(node_id)] = (float(x), float(y))
        elif line.startswith('element'):
            _, _, *nodes = line.split()
            element_connectivity.append([int(node) for node in nodes])

    return node_coords, element_connectivity


# Define model parameters
E = 200000  # Young's Modulus (MPa)
nu = 0.3  # Poisson's Ratio
thickness = 0.015  # Plate thickness (m)
thickness = thickness * 1000    # Plate thickness (mm)

# Steel Example
# E = 200000  # Young's Modulus (MPa)
# nu = 0.3  # Poisson's Ratio
# thickness = 15  # Plate thickness (mm)

# Define model
model = ops.model('basic', '-ndm', 2, '-ndf', 2)

# Read node coordinates and element connectivity from mesh file
node_coords, element_connectivity = read_mesh_file('mesh_file')

# Define nodes
for node_id, (x, y) in node_coords.items():
    ops.node(node_id, x, y, 0)

# Define material
ops.nDMaterial('ElasticIsotropic', 1, E, nu)

# Define elements
for i, nodes in enumerate(element_connectivity, start=1):
    ops.element('Tri31', i, *nodes[1:4], thickness, 'PlaneStress', 1, -10)  # Using material tag 1

# Function to apply load along the top edge
def apply_load_top_edge():
    # Define load pattern
    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1)

    # UDL - Define loads at top edge nodes
    # max_y_coord = max(node_coords.values(), key=lambda x: x[1])[1]
    # min_y_coord = max(node_coords.values(), key=lambda x: x[0])[1]
    # btm_edge_nodes = [node_id for node_id, (x, y) in node_coords.items() if y == min_y_coord]
    # top_edge_nodes = [node_id for node_id, (x, y) in node_coords.items() if y == max_y_coord]
    # print(len(top_edge_nodes))
    # y_load = -15  # kN/m
    # y_load_to_nodes = (y_load * 5) / len(top_edge_nodes)

    # # Cantilever Beam Example
    ops.fix(1, 1, 1, 1)
    ops.fix(4, 1, 1, 1)

    y_load = -15  # kN
    ops.load(3, 0, y_load)


# Function to apply normal load to the plate
def apply_normal_load():
    # Define load pattern
    ops.timeSeries('Linear', 2)
    ops.pattern('Plain', 1, 1)

    # Define loads normal to the plate
    for node_id, _ in node_coords.items():
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
opsvis.plot_load()
plt.figure()
sig_out = opsvis.sig_out_per_node("all")

# j, jstr = 0, 'sxx'
j, jstr = 3, 'vmis'
nds_val = sig_out[:, j]
min_val = np.min(nds_val)
max_val = np.max(nds_val)
plt.title(f"{jstr}, Min: {min_val:.2f}, Max: {max_val:.2f}")
opsvis.plot_stress_2d(nds_val)
plt.box(False)
# Show plot
plt.show()

opsvis.plot_defo(unDefoFlag=1)
plt.axis('equal')

plt.show()
