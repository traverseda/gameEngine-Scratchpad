from pyglet.gl import *

def cubeCreator(coords0):
    x,y,z=coords0
    X,Y,Z=(x+1,y+1,z+1)

    return (4,GL_QUADS,None,('v3f',(x,y,z, X,y,z, X,Y,z, x,Y,z)))
    

class NaiveBlockRenderer():
    '''
This renders the geometry it gets from blocks.
Why pass geometry to the renderer instead of having the blocks
render directly, especially since our BlockWorld object is doing so much work to
occlude hidden blocks?

Cacheing, and eventually mesh simplifcation.

A 4x4x4 cube of blocks has 48 faces. With mesh simplification we can bring that
down to 12 losslessly.

Passing a bunch of connected blocks to a block renderer should *significantly* increase
the number of blocks we can have on screen at one time.
    '''
    def __init__(self):
        pass
    def drawCube(self):
        color=('c3f',(1,1,1)*4)
        return (*cubeCreator((0,0,0)), color)

class TextureGroup():
    '''
    A group of textures all stored together.
    '''
    def __init__(self):
        coords={} #Give it the name of a texture and it will return the coords in pixels.
        pass

class Block():
    pass

    def _getGeometry_():
        pass
