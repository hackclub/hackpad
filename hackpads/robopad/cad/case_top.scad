include <BOSL2/std.scad>

module case_top() {
    overlapBuffer = 0.1;
    height = 1.5;
    
    difference() {
        union() {
            cuboid([120, 120, height], rounding=1, except=BOTTOM);
            translate([-30, 30, height + 2.5]) cylinder(r=17, h=height + 5, center=true);
            translate([30, 30, height + 2.5]) cylinder(r=17, h=height + 5, center=true);
        }

        translate([-30, 30, 0]) cylinder(r=15, h=30+overlapBuffer, center=true);
        translate([30, 30, 0]) cylinder(r=15, h=30+overlapBuffer, center=true);
        translate([38, -17.5, 0]) cube([10, 47, height + overlapBuffer], center=true);
        translate([-37, -17.5, 0]) cube([10, 47, height + overlapBuffer], center=true);
        for (i=[0:1:2]) {
            for (j=[-2:1:0]) {
                translate([i * 19.05 - 18.1706, j * 19.05 + 3.5719, 0]) cube([14, 14, height + overlapBuffer], center=true);
            }
        }
        
        translate([55, -55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);
        translate([-55, -55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);
        translate([-55, 55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);
        translate([55, 55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);
        translate([0, -50, 0.5]) linear_extrude(1+overlapBuffer) text("robopad, made proudly by urjith mishra (thescientist101 on gh)", size=2, halign="center", valign="center", font="Arial:style=Bold", $fn=100);
    }
}

translate([0, 0, 5])  case_top();
color("green") import("./components/pcb.stl");