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

        translate([-59, 0, 0]) rotate([-90, 180, 90]) linear_extrude(1+overlapBuffer) text("robopad, made proudly by urjith mishra (thescientist101 on gh)", size=2, halign="center", valign="center", font="Arial:style=Bold", $fn=100);
    }
}

translate([0, 0, -1.5]) case_bottom();
color("green") import("./components/pcb.stl");