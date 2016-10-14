from parse import compile
import concurrent.futures
import sys, asyncio, math

'''
The file with a big chunk of our geometry functions.

The basic conceit of this is sets of co-ordinates (or keys).

Calling .cube((0,0,0),(20,20,20)) returns a 20*20*20 cube
'''

def distance(point1, point2):
    diff1 = point1[0]-point2[0]
    diff1 = diff1**2
    diff2 = point1[1]-point2[1]
    diff2 = diff2**2
    return math.sqrt(diff1+diff2)

def cubeGenerator(center, size, partial=list()):
    depth = len(partial)
    if depth < 3:
        for i in range(center[depth],center[depth]+size[depth]):
            newPartial = partial+[i,]
            yield from cubeGenerator(center,size,newPartial)
    else:
        partial = tuple(partial)
        yield partial
def cylinderGenerator(center, rad, height, partial=list()):
    pass

class World():
    parseX=compile("{:d}x")
    parseY=compile("{:d}Y")
    parseZ=compile("{:d}Z")
    def __init__(self, storage=dict(), blocksize=64, default=None):
        self.storage=storage
        self.blocksize=blocksize
        self.default=default
    def __getitem__(self, key):
        key = self.keyFormat(key)
        if key in self.storage:
            return self.storage[key]
        else:
            return self.default
    def __setitem__(self, key, value):
        key = self.keyFormat(key)
        self.storage[key] = value
    def __delitem__(self, key):
        key = self.keyFormat(key)
        del self.storage[key]

    def cube(self, corner, size, center=False):
        if center==True:
            #Floor it? Or use the default "round" which jumps to nearest even number?
            #Round will make tesselating even-rad objects easier.
            
            corner=(corner[0]-(size[0]/2),corner[1]-(size[1]/2),corner[1]-(size[1]/2))
            corner = [round(i) for i in corner]
        return set(cubeGenerator(corner, size))
 
    def sphere(self, center, diam):
        rad=diam/2
        boundingCube = self.cube(center, (diam,diam,diam), center=True)
        return set((i for i in boundingCube if distance(center, i) < rad ))

    def normalize(self, position):
        """ Accepts `position` of arbitrary precision and returns the block
        containing that position.
        Parameters
        ----------
        position : tuple of len 3
        Returns
        -------
        block_position : tuple of ints of len 3
        """
        x, y, z = position
        x, y, z = (int(round(x)), int(round(y)), int(round(z)))
        return (x, y, z)

    def keyFormat(self, *args):
        '''
        This formats a key for our hashmap.
        It accepts keys either as strings, or as
        tuples, and returns a tuple.

            "1x2y3z" = (1,2,3,0)
        '''
        if len(args) == 1 and type(args[0])==str:
            x=self.parseX.search(args[0])[0]
            y=self.parseY.search(args[0])[0]
            z=self.parseZ.search(args[0])[0]
        elif len(args)==3:
            x=args[0]
            y=args[1]
            z=args[2]
        else:
            raise Exception("Can't parse", *args) 
        return (x,y,z)
