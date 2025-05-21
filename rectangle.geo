lc = 0.25;
width = 8.0;
length = 3.0;

Point(1) = {0, 0, 0, lc};
Point(2) = {width, 0, 0, lc};
Point(3) = {width, length, 0, lc};
Point(4) = {0, length, 0, lc};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Line Loop(5) = {1, 2, 3, 4};
Mesh.Algorithm = 8;
Plane Surface(6) = {5};
Recombine Surface {6};
