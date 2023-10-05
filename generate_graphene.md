## How to generate your coordinates?

* use VMD
* use Python


### VMD
open `Extensions > Modeling > Nanotube Builder `  
make sure to not include `Bonds, Angles, ...`  
for carbon length of bond is `0.142 nm`


you should see something like:  
 `calling graphene_core -lx 10 -ly 10 -type zigzag -nlayers 1 -b 0 -a 1 -d 1 -i 1 -cc 0.142 -ma C-C`


**THEN** you should open VMD console (Extensions) and get output with:  

```

# ---------- find out sizes -------------

set all [atomselect top all]

set dimensions [measure minmax $all]

# Access the first set of coordinates
set first_coordinates [lindex $dimensions 0]
set x1 [lindex $first_coordinates 0]
set y1 [lindex $first_coordinates 1]
set z1 [lindex $first_coordinates 2]

# Access the second set of coordinates
set second_coordinates [lindex $dimensions 1]
set x2 [lindex $second_coordinates 0]
set y2 [lindex $second_coordinates 1]
set z2 [lindex $second_coordinates 2]

# Print the values
puts "First coordinates: x=$x1, y=$y1, z=$z1"
puts "Second coordinates: x=$x2, y=$y2, z=$z2"


# ------------- define box sies -----------------

molinfo top set a [expr {$x2 - $x1}]
molinfo top set b [expr {$y2 - $y1}]
molinfo top set c [expr {$z2 - $z1}]


# --------------- write out as lammps data -------------

molinfo top set c 100

topo writelammpsdata graphene.data atomic

```


###