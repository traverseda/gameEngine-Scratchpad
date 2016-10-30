A bunch of random musings, more or less stream of consiousness. Almost definitely not worth reading.

---

What should our base engine objects be?

 * A voxel storage system?

 * A processor that simplifies geometry?
   * I belive we can get a *lot* better performance then minecraft with some pretty simple simplification.

 * A texture-group creator?

 * A flexbox-style system for placing UI widgets

 * A "view", being a player window, or a portal, or an api endpoint.

 * A physics-world
   * We can try and get physics information from the mesh simplifier. Easier for stuff like voxels.

The basic flow is that a voxel storage system (VSS) contains information about an object.

A renderer calls the "draw" function on a VSS for a given coord. A VSS calls the "draw" function on the object at the coord.

Our view calls the render function on the renderer.

[](/ "Made using http://asciiflow.com/")
```
                   +-------------------+
                   |Texture Group Cache|
                   +--^----------------+
                      |
                      |
+-+ Voxel Storage     |                                 +-+
|   +-----------------+---+ +---------------------+       |
|   |Block Object Instance| |Block Object Instance| ...   |
|   +------------^--------+ +---------------------+       |
+-+              |                                      +-+
                 |
                 |
          +------+--------+   +-------------+
          |Mesh Simplifier<---+Physics World|
          |and Renderer   |   +-----^-------+
          +------------^--+         |
                       |            |
                       |            |
                       |            |
                       |            |
                       +-+----+-----+
                         |View|
                         +----+

```
