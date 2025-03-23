bottomLayerH = 5;
middleLayerH = 15;
topLayerH = 3;
/*
linear_extrude(height = bottomLayerH) {
    import(file = "case_layers.svg", layer = "back");
}
translate([0, 0, bottomLayerH]) {
    linear_extrude(height = middleLayerH) {
        import(file = "case_layers.svg", layer = "middle");
    }
}
*/
translate([0, 0, bottomLayerH + middleLayerH]) {
    linear_extrude(height = topLayerH) {
        import(file = "case_layers.svg", layer = "top");
    }
}


if(false){
    color("green")
    if(false){
        translate([0, 0, bottomLayerH + middleLayerH-10])
        import("Untitled.stl");}
    else{
        translate([0, 0, bottomLayerH + middleLayerH-5])
        linear_extrude(3)
        import(file = "case_layers.svg", layer = "pcb");
    }
}