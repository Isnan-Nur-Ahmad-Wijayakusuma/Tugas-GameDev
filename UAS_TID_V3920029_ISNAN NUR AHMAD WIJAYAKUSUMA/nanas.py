from math import pi, sin, cos
from direct.interval.FunctionInterval import ScaleInterval
import pygame

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

from panda3d.core import *
from pygame.constants import SCALED
loadPrcFileData("", "audio-library-name p3openal_audio")

from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText


# digunakan untuk mengatur posisi, style, dan ukuran dari text
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(0, 0, 0, 1),
                        parent=base.a2dTopLeft, align=TextNode.ALeft,
                        pos=(0.08, -pos - 0.04), scale=.06)

# digunakan untuk mengatur posisi, style, dan ukuran dari text
def addTitle(text):
    return OnscreenText(text=text, style=1, pos=(-0.1, 0.09), scale=.08,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        fg=(1, 1, 1, 1))

class Myapp(ShowBase):
    def __init__(self):
        super().__init__(self)

        # membuat text yang akan ditampilkan di layar
        self.title = addTitle("Panda3D: Animation Nanas")
        self.inst1 = addInstructions(0.06, "P: Play/Pause Music")
        self.inst2 = addInstructions(0.12, "S: Stop and Rewind Music")

        # mengimport model dan mengatur posisi serta ukuran model
        self.car = self.loader.load_model("nanas.obj")
        self.car.reparentTo(self.render)
        self.car.setScale(0.3, 0.3, 0.3)
        self.car.setPos(0, 0, -1)

        # menggunakan task manager untuk mengatur pergerakan kamera
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # menerima perintah inputan dari keyboard
        self.accept('p', self.playpause)
        self.accept('P', self.playpause)
        self.accept('s', self.stopsound)
        self.accept('S', self.stopsound)
        

        # mengimport music backsound
        self.sound = loader.loadSfx("Naruto.ogg")
    
    # memebuat fungsi stop music
    def stopsound(self):
        self.sound.stop()
        self.sound.setPlayRate(1.0)

    # memebuat fungsi play music
    def playpause(self):
        
            self.sound.play()
    
    

    # memebuat fungsi atur volume music
    def volume(self, nilai):
        v = float(nilai)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(v)
    
    # memebuat fungsi silinder bottom untuk mengatur volume music, tetapi masih error dan tidak terpanggil
    def slider(self):
        w1 = SCALED(from_=0.00, to=1.0, resolution=0.01, command=self.volume,
                   orient=HORIZONTAL, length=300, label='Volume :', showvalue=0)
        w1.pack()
        w1.set(0.50)


    # fungsi untuk menggerakan kamera dengan mengatur putaran kamera 180 dikali dengan jumlah pi dan pergerakan kecepatan kamera
    def spinCameraTask(self, task):
        angleDegrees = task.time * 8
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

# menjalankan class myapp
app = Myapp()
app.run()