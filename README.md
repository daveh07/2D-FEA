# FEA-Plate
- Uses Opensees Finite Element open source API for structural analysis of 2D shapes
- Implemented a Python PySide6 GUI application that meshes user geometry for analysis
- Runs analysis and plots outputs for material stress and strain for loading conditions
- Currently implemented a 3D model and rendering using VTK

### EXAMPLES
- Run quad_mesh.py and input dimensions and render plate, example 8m Width, 3m Height, 0.25m thickness
- Choose a mesh size, eg) 0.25

- A mesh file is generated:
![image](https://github.com/user-attachments/assets/40ec8762-5842-484f-9d3f-5631b319c9a2)


- This mesh file is used in the file, op_quad_model.py & cantilever_quads.py
- Run either file and press 1 to apply load along top edge. (Other loading criteria is currently being implemented)

- Eg) Output for cantilever_quads.py:
- Von Mises bending Stress:
![image](https://github.com/user-attachments/files/14080123/082c802e-4e78-40c9-9823-a091883b4e71.png)
- Beam Deflection:
![Screenshot From 2025-05-21 21-08-38](https://github.com/user-attachments/files/14080123/a118f776-c20c-4e9c-a0a4-54d2522f7c71.png)

### Tri Element Example
- Run main.py
- Input 6m width, 4m height, 0.25m thickness for the plate and render plate
- 0.15 for mesh size and generate mesh.
![Screenshot From 2025-05-21 21-09-51](https://github.com/user-attachments/files/14080123/c3e5a657-8894-45d6-973e-8e82c3a577d1.png)

- Run cantilever_beam.py, this file uses the tri mesh file generated.
- Press 1 to apply load at top edge.
- Von Mises Stress:
![Screenshot From 2025-05-21 21-12-24](https://github.com/user-attachments/files/14080123/d0ee506b-a00a-4282-99b7-9eb832d58088.png)

- Mesh and Loading:
![Screenshot From 2025-05-21 21-13-00](https://github.com/user-attachments/files/14080123/e52de52e-4b1a-459b-8886-87f6bccf66bc.png)

- Deflection:
![Screenshot From 2025-05-21 21-13-25](https://github.com/user-attachments/files/14080123/1393a76b-e41a-4b45-addb-86307e98aa20.png)
