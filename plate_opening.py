import subprocess
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mesh Generator")
        layout = QVBoxLayout()

        # Button to generate mesh
        mesh_button = QPushButton("Generate Mesh")
        mesh_button.clicked.connect(self.generate_mesh)
        layout.addWidget(mesh_button)

        self.setLayout(layout)

    def generate_mesh(self):
        # Run Gmsh subprocess to generate the mesh
        process = subprocess.Popen(["gmsh", "rectangle_opening.geo", "-2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Mesh generated successfully.")
            # Display the mesh using Gmsh's built-in viewer
            subprocess.Popen(["gmsh", "rectangle_opening.msh"])
        else:
            print("Error:", stderr.decode())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
