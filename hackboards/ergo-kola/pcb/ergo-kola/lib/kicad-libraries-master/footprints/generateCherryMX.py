import os
import itertools

sizesToGenerate=["1.00", "1.25", "1.50", "1.75", "2.00", "2.25", "2.50", "2.75", "3.00", "4.00", "4.50", "5.50", "6.00", "6.25", "6.50", "7.00", "8.00", "9.00", "9.75", "10.00"]

# All of the dimensions are in mm
unit = 19.05

# Spacings taken from https://cdn.sparkfun.com/datasheets/Components/Switches/MX%20Series.pdf and https://deskthority.net/wiki/Space_bar_dimensions
stabSpacings = {
  "2.00": 0.94*25.4,
  "2.25": 0.94*25.4,
  "2.50": 0.94*25.4,
  "2.75": 0.94*25.4,
  "3.00": 1.5*25.4,
  "4.00": 2.25*25.4,
  "4.50": 2.73*25.4,
  "5.50": 3.375*25.4,
  "6.00": 3*25.4,
  "6.25": 100,
  "6.50": 4.125*25.4,
  "7.00": 4.5*25.4,
  "8.00": 5.25*25.4,
  "9.00": 5.25*25.4,
  "9.75": 5.25*25.4,
  "10.00": 5.25*25.4,
}

componentsList = {
  "BaseStart": """
(module {name} (layer F.Cu) (tedit 5E866FEB)
  (descr "{description}")
  (tags "{keywords}")
  (fp_text reference REF** (at 0 -8.6625) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value {name} (at 0 8.6625) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_line (start 7 7) (end -7 7) (layer F.SilkS) (width 0.12))
  (fp_line (start 7 -7) (end 7 7) (layer F.SilkS) (width 0.12))
  (fp_line (start -7 -7) (end 7 -7) (layer F.SilkS) (width 0.12))
  (fp_line (start -7 -7) (end -7 7) (layer F.SilkS) (width 0.12))
  (fp_line (start -7.8 -7.8) (end 7.8 -7.8) (layer F.Fab) (width 0.12))
  (fp_line (start -7.8 -7.8) (end -7.8 7.8) (layer F.Fab) (width 0.12))
  (fp_line (start 7.8 -7.8) (end 7.8 7.8) (layer F.Fab) (width 0.12))
  (fp_line (start -7.8 7.8) (end 7.8 7.8) (layer F.Fab) (width 0.12))
  (fp_line (start -{outlineSize} 9.525) (end -{outlineSize} -9.525) (layer Dwgs.User) (width 0.12))
  (fp_line (start {outlineSize} 9.525) (end -{outlineSize} 9.525) (layer Dwgs.User) (width 0.12))
  (fp_line (start {outlineSize} -9.525) (end {outlineSize} 9.525) (layer Dwgs.User) (width 0.12))
  (fp_line (start -{outlineSize} -9.525) (end {outlineSize} -9.525) (layer Dwgs.User) (width 0.12))
  (pad "" np_thru_hole circle (at 0 0) (size 4 4) (drill 4) (layers *.Cu *.Mask))""",

  "Pins": """
  (pad 1 thru_hole circle (at -3.81 -2.54) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))
  (pad 2 thru_hole circle (at 2.54 -5.08) (size 2.2 2.2) (drill 1.5) (layers *.Cu *.Mask))""",

  "PCB": """
  (pad "" np_thru_hole circle (at -5.08 0) (size 1.75 1.75) (drill 1.75) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at 5.08 0) (size 1.75 1.75) (drill 1.75) (layers *.Cu *.Mask))""",

  "KailhSocket": """
  (pad "" np_thru_hole circle (at -3.81 -2.54) (size 3 3) (drill 3) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at 2.54 -5.08) (size 3 3) (drill 3) (layers *.Cu *.Mask))
  (pad 1 smd rect (at -7.41 -2.54) (size 2.55 2.5) (layers B.Cu B.Paste B.Mask))
  (pad 2 smd rect (at 6.015 -5.08) (size 2.55 2.5) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/KailhSocket.stp"
    (offset (xyz -0.6 3.8 -3.5))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 180))
  )""",

  "LED": """
  (pad 3 thru_hole circle (at -1.27 5.08) (size 1.6906 1.6906) (drill 0.9906) (layers *.Cu *.Mask))
  (pad 4 thru_hole circle (at 1.27 5.08) (size 1.6906 1.6906) (drill 0.9906) (layers *.Cu *.Mask))""",

  "LTST-A683CEGBW": """
  (fp_line (start -1.7 3.25) (end -2 3.25) (layer B.SilkS) (width 0.12))
  (fp_line (start -2 3.25) (end -2 3.55) (layer B.SilkS) (width 0.12))
  (fp_line (start -1.7 3.55) (end 1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 3.55) (end 1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 6.55) (end -1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start -1.7 6.55) (end -1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (pad 3 smd rect (at -2.6 4.3) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 4 smd rect (at -2.6 5.8) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 5 smd rect (at 2.6 4.3) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 6 smd rect (at 2.6 5.8) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/LTST-A683CEGBW.step"
    (offset (xyz 0 -5.05 -1.87))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 0))
  )""",

  "LTST-A683CEGBW-HS": """
  (fp_line (start -1.7 3.25) (end -2 3.25) (layer B.SilkS) (width 0.12))
  (fp_line (start -2 3.25) (end -2 3.55) (layer B.SilkS) (width 0.12))
  (fp_line (start -1.7 3.55) (end 1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 3.55) (end 1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 6.55) (end -1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start -1.7 6.55) (end -1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (pad 3 smd rect (at -2.95 4.1) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (pad 4 smd rect (at -2.95 6) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (pad 5 smd rect (at 2.95 4.1) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (pad 6 smd rect (at 2.95 6) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/LTST-A683CEGBW.step"
    (offset (xyz 0 -5.05 -1.87))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 0))
  )""",

  "LTST-A683CEGBW-Rotated": """
  (fp_line (start 1.7 6.85) (end 2 6.85) (layer B.SilkS) (width 0.12))
  (fp_line (start 2 6.85) (end 2 6.55) (layer B.SilkS) (width 0.12))
  (fp_line (start -1.7 3.55) (end 1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 3.55) (end 1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 6.55) (end -1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start -1.7 6.55) (end -1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (pad 6 smd rect (at -2.6 4.3) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 5 smd rect (at -2.6 5.8) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 4 smd rect (at 2.6 4.3) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (pad 3 smd rect (at 2.6 5.8) (size 1.8 0.9) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/LTST-A683CEGBW.step"
    (offset (xyz 0 -5.05 -1.87))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 180))
  )""",

  "LTST-A683CEGBW-Rotated-HS": """
  (fp_line (start 1.7 6.85) (end 2 6.85) (layer B.SilkS) (width 0.12))
  (fp_line (start 2 6.85) (end 2 6.55) (layer B.SilkS) (width 0.12))
  (fp_line (start -1.7 3.55) (end 1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 3.55) (end 1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start 1.7 6.55) (end -1.7 6.55) (layer Edge.Cuts) (width 0.05))
  (fp_line (start -1.7 6.55) (end -1.7 3.55) (layer Edge.Cuts) (width 0.05))
  (pad 6 smd rect (at -2.95 4.1) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (pad 5 smd rect (at -2.95 6) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (pad 4 smd rect (at 2.95 4.1) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (pad 3 smd rect (at 2.95 6) (size 2.5 1.1) (layers B.Cu B.Paste B.Mask))
  (model "${{KIPRJMOD}}/models/LTST-A683CEGBW.step"
    (offset (xyz 0 -5.05 -1.87))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 180))
  )""",

  "StabWireTop": """
  (pad "" np_thru_hole circle (at -{stabSpacing} 7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at -{stabSpacing} -8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} -8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} 7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))""",

  "StabWireBottom": """
  (pad "" np_thru_hole circle (at -{stabSpacing} -7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at -{stabSpacing} 8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} 8.24) (size 4 4) (drill 4) (layers *.Cu *.Mask))
  (pad "" np_thru_hole circle (at {stabSpacing} -7) (size 3.05 3.05) (drill 3.05) (layers *.Cu *.Mask))""",

  "BaseEnd": """
)"""
}

variants = [
  [None, "PCB"],
  ["Pins", "KailhSocket"],
  [None, "StabWireTop", "StabWireBottom"],
  [None, "LED", "LTST-A683CEGBW", "LTST-A683CEGBW-Rotated", "LTST-A683CEGBW-HS", "LTST-A683CEGBW-Rotated-HS"],
]

def generateFootprints():
  for variant in itertools.product(*variants):
    # Filter None values
    components = [component for component in variant if component is not None]

    # Create directory containing all sizes of given variant
    dirname = f"CherryMX_{'_'.join(components)}.pretty".replace("_Pins", "")
    os.makedirs(dirname, exist_ok = True)

    for size in sizesToGenerate:
      if size not in stabSpacings and ("StabWireTop" in components or "StabWireBottom" in components):
        continue

      name = f"CherryMX_{size}u_{'_'.join(components)}".replace("_Pins", "")

      # Generate description
      mountType = "PCB" if "PCB" in components else "Plate"

      usingKailhSocket = "yes" if "KailhSocket" in components else "no"

      stabilizer = (
        "n/a" if float(size) < 2 else (
          "PCB mounted (Wire Top)" if "StabWireTop" in components else (
            "PCB mounted (Wire Bottom)" if "StabWireBottom" in components else "Plate mounted"
          )
        )
      )
      
      lighting = "none"
      lightingMap = {
        "LTST-A683CEGBW": "LTST-A683CEGBW",
        "LTST-A683CEGBW-Rotated": "LTST-A683CEGBW (rotated)",
        "LTST-A683CEGBW-HS": "LTST-A683CEGBW for hand-soldering",
        "LTST-A683CEGBW-Rotated-HS": "LTST-A683CEGBW (rotated) for hand-soldering",
        "LED": "2 pin LED"
      }
      
      for component in components:
        if component in lightingMap:
          lighting = lightingMap[component]
          break

      description = "Cherry MX switch footprint. "
      description += f"Size: {size}u"
      description += f", Mount type: {mountType}"
      description += f", Using Kailh Socket: {usingKailhSocket}"
      description += f", Stabilizer: {stabilizer}"
      description += f", Lighting: {lighting}"

      keywords = name.replace("_", " ")

      # Generate output code
      code = ""
      for component in ["BaseStart", *components, "BaseEnd"]:
        code += componentsList[component].format(
          name=name, 
          description=description, 
          keywords=keywords, 
          outlineSize=float(size) * unit / 2, 
          stabSpacing=stabSpacings[size] / 2 if size in stabSpacings else "",
        )

      # Save footprint to file
      file = open(f"{dirname}/{name}.kicad_mod", "w+")
      file.writelines(code)
      file.close()

      print(f"Generated: {name}.kicad_mod")

generateFootprints()