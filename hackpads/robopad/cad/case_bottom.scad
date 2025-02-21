include <BOSL2/std.scad>

module case_bottom() {
    overlapBuffer = 0.1;
    difference() {
        cuboid([120, 120, 13], rounding=1, except=TOP);
        translate([0, 0, 3]) cube([101, 101, 10 + overlapBuffer], center=true);
        translate([55, -55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);
        translate([-55, -55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);
        translate([-55, 55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);
        translate([55, 55, 0]) cylinder(r=1.7, h=13+overlapBuffer, center=true);

        translate([0, 55, -1.5]) cuboid(size=[10, 10+overlapBuffer, 4], rounding=1, except=[FRONT, BACK]);
    }
}

translate([0, 0, -1.5]) case_bottom();
color("green") import("./components/pcb.stl");