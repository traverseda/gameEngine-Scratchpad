from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse
import pyglet
import settings, asyncio

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.batch=pyglet.graphics.Batch()
        self.label = pyglet.text.Label("abc", font_size=self.height,
                          batch=self.batch,
                          x=self.width/2, y=self.height/2,
                          anchor_x="center", anchor_y="center")

    def on_resize(self, *args, **kwargs):
        super(Window, self).on_resize(*args, **kwargs)
        print(args)

    def update(self, dt):
        self.dispatch_events()
        self.clear()
        self.batch.draw()
        self.flip()

import time
async def draw_frame(display):
    t = time.time()
    while True:
        newT=time.time()
        display.update(t-newT)
        t=newT
        await asyncio.sleep(1/settings.FRAMES_PER_SEC)
