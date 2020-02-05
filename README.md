# setup_retopo
A Blender 2.8x script for getting a plane into a retopo setup quickly

1) Select Mesh to Retopolgize
2) Search for the "Setup Retopo From New Plane" operator
3) The following tasks are run

  * Retopo Geometry is Created and moved the plane out to a selectable Y distance
  * Selectable Add Shrinkwrap with inactive selected mesh as Target
    * Selectable Set Show on cage View for Shrinkwrap
  * Selectable Add Mirror modifier -with offset of plane (clipping on)
  * Set Object to "Show in Front"
  * Set Object color to selectable color
  * Turn on Snapping
    * Set Snapping to Face
    * Set "Project Individual Elements" in snapping
  * Set the Viewport shading to solid
    * Set the window shading color type to object
    * Turns on Backface culling
  * Adds Automerge
  * Sets the high-res mesh as non-selectable
