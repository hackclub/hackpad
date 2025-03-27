pcb_size = [133.35,359.56875,1.6];
tolerance = 0.5;
case_thickness = 5;
angle = 5;


module pcb(){
    
    cube(pcb_size);
}

module case(){
    difference() {
        union() {
            cube(
                pcb_size +
                [
                    case_thickness/2,
                    case_thickness,
                    case_thickness
                ]
            );

            case_feet();
        }
        
        translate([case_thickness/2,
                case_thickness/2-tolerance/2,
                case_thickness/2-tolerance/2]) 
        cube(pcb_size+[0,tolerance,tolerance]);

        translate([case_thickness,
                case_thickness,
                -500]) 
        cube(pcb_size-[case_thickness/2,case_thickness,0]+ [0,0,10000]);
    }

}

module case_feet() {
  /*
        /
       |\    /     /
       | \  /     /
       \  \/     /___
   |    \ |      
  a|     \|___________
          
          |--b-- ... ---|

  */

    top_piece_d = pcb_size.x  + case_thickness/2;

    top_piece_h = pcb_size.z + case_thickness;
    top_piece_w = pcb_size.y + case_thickness;

    a = cos(angle) * top_piece_h;
    b = cos(angle) * top_piece_d + sin(angle) * top_piece_h;
    
    difference() {
        translate([0,0,top_piece_h]) 
        rotate([0,90+angle,0]) 
        cube([a,top_piece_w,b]);
    }

}






rotate([0,-angle,0]){
    color(c = "green") 
   pcb();

translate([-case_thickness/2,-case_thickness/2,-case_thickness/2]) 
case();

}