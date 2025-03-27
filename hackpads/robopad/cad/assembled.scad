use <case_bottom.scad>
use <case_top.scad>

translate([0, 0, 5]) case_top();
translate([0, 0, -1.5]) case_bottom();
color("green") import("./components/pcb.stl");