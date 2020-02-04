# setup_retopo
A Blender 2.8x script for getting a plane into a retopo setup quickly

1) Add a plane
2) Search for the "Setup Retopo" operator
3) The following tasks are run

  * Rotate the plane 90 degrees and move the plane out to (1,5,0)
  * Reset origin to 3d cursor
  * Apply transform
  * Add Mirror modifier
  * Set clipping on for mirror modifier
  * Set Object to "Show in Front"
  * Set Object color to a randomish teal color
  * Turn on Snapping
  * Set Snapping to Face
  * Set "Project Individual Elements" in snapping
  * Set the Viewport shading to solid
  * Set the window shading color type to object
  * Turns on Backface culling

After the add-on is run you can change the Y position of the new plane and the object color
