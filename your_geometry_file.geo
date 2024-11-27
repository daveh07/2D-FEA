
        lc = 12.0;
        width = 5.0;
        length = 3.1;
    
        // Define outer rectangle
        Point(1) = {0, 0, 0, lc};
        Point(2) = {width, 0, 0, lc};
        Point(3) = {width, length, 0, lc};
        Point(4) = {0, length, 0, lc};
    
        Line(1) = {1, 2};
        Line(2) = {2, 3};
        Line(3) = {3, 4};
        Line(4) = {4, 1};
    
        Line Loop(5) = {1, 2, 3, 4};
        Plane Surface(6) = {5};
        Recombine Surface {6};
    
        // Define inner rectangle for the hole
        inner_width = 1.0;
        inner_length = 1.0;
    
        Point(5) = {(width - inner_width) / 2, (length - inner_length) / 2, 0, lc};
        Point(6) = {(width + inner_width) / 2, (length - inner_length) / 2, 0, lc};
        Point(7) = {(width + inner_width) / 2, (length + inner_length) / 2, 0, lc};
        Point(8) = {(width - inner_width) / 2, (length + inner_length) / 2, 0, lc};
    
        Line(5) = {5, 6};
        Line(6) = {6, 7};
        Line(7) = {7, 8};
        Line(8) = {8, 5};
    
        Line Loop(9) = {5, 6, 7, 8};
        Plane Surface(10) = {9};
        Recombine Surface {10};
    
        // Physical Surface
        Physical Surface("Hole") = {10};
        