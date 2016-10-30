from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse
import pyglet
import settings, asyncio, math
import gameObjects.basics as basics

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.batch=pyglet.graphics.Batch()
        self.label = pyglet.text.Label("abc", font_size=self.height,
                          batch=self.batch,
                          x=self.width/2, y=self.height/2,
                          anchor_x="center", anchor_y="center")
        self.renderer=basics.NaiveBlockRenderer()
        self.position=(0,0,0)
        self.rotation=(0,0)
    def on_resize(self, *args, **kwargs):
        super(Window, self).on_resize(*args, **kwargs)
        print(args)

    def update(self, dt):
        self.clear()
        self.set_3d()
        self.set_2d()
        self.dispatch_events()
        self.batch.draw()
#        self.batch.add(*self.renderer.drawCube())
        self.flip()

    def set_2d(self):
        """ Configure OpenGL to draw in 2d.
        """
        width, height = self.get_size()
        glDisable(GL_DEPTH_TEST)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set_3d(self):
        """ Configure OpenGL to draw in 3d.
        """
        width, height = self.get_size()
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, width / float(height), 0.1, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        x, y = self.rotation
        glRotatef(x, 0, 1, 0)
        glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
        x, y, z = self.position
        glTranslatef(-x, -y, -z)

import time
async def draw_frame(display):
    t = time.time()
    while True:
        newT=time.time()
        display.update(t-newT)
        t=newT
        await asyncio.sleep(1/settings.FRAMES_PER_SEC)
