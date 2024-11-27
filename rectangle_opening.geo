lc = 12.0;
width = 5.0;
length = 3.1;
hole_radius = 1.0;  # Radius of the hole

// Define outer rectangle
Point(1) = {0, 0, 0, lc};
Point(2) = {width, 0, 0, lc};
Point(3) = {width, length, 0, lc};
Point(4) = {0, length, 0, lc};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};`

Line Loop(5) = {1, 2, 3, 4};
Plane Surface(6) = {5};

// Define points for the hole
Point(5) = {width/2, length/2, 0, lc};

// Define circle for the hole
Circle(7) = {5, hole_radius};

// Create line loop for the hole
Line Loop(8) = {7};

// Create surface for the hole
Plane Surface(9) = {8};

// Subtract the hole from the outer rectangle
Surface Loop(10) = {6, 9};
Volume(11) = {10};

Recombine Surface {6, 9};
