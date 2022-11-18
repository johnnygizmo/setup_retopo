# setup_retopo
A Blender 3.3.x script for getting a plane into a retopo setup quickly

1) Select Mesh to Retopolgize (Make sure it is centered around the origin.
2) Search for the "Setup Retopology" operator
3) The following tasks are run

  * Retopo Geometry is Created and moved out to a selectable Y distance
  * Selectable Add Shrinkwrap with target mesh
  * Selectable Add Mirror modifier with offset of plane (clipping on)
  * Subsurf Modifier in object mode only
  * Set Object to "Show in Front"
  * Set Object color to selectable color
  * Turn on Snapping
    * Set Snapping to Face
    * Set "Project Individual Elements" in snapping
  * Set the Viewport shading to solid
    * Set the window shading color type to object
    * Turns on Backface culling
    * Hidden Wire Shading
    * Fade Inactive Objects
  * Adds Automerge with selectable distance

4) Use the settings popup to change the settings (especially the plane scale) to your needs
