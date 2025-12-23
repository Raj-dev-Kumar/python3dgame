
import system
from panda3d.core import ClockObject
import math
import const

class Bullet:
    def __init__(self, base, render, loader, timenow, initialpos=None,dirx=0,diry=0):
        self.base = base
        self.render = render
        self.loader = loader
        self.timenow = timenow
        self.timevanish = self.timenow + 5
        self.initialpos = initialpos
        self.remove = False
        self.dirx = dirx
        self.diry = diry

        self.bullet = loader.loadModel(system.get_model_path("sniper_bullet.glb"))    
        self.bullet.reparentTo(render)
        self.bullet.setScale(0.1) 
        self.bullet.setPos(initialpos[0], initialpos[1], initialpos[2])  


    def update(self,frametime):
        if self.timevanish<frametime:
            self.bullet.removeNode()
            self.remove = True
            #del self        
      #  self.moveBullet()

    def moveBullet(self,dt):
        heading = math.degrees(math.atan2(self.dirx, self.diry))
        self.bullet.setHpr(heading,0,0)
        print(f"BULLET : dirx ={self.dirx} diry={self.diry} ax = {math.asin(self.dirx)} ay={math.acos(self.diry)} ")
        tamanho = math.sqrt(self.dirx*self.dirx + self.diry*self.diry)
        if self.bullet.getX() < self.initialpos[0]+256:
            self.bullet.setX(self.bullet.getX()-40*dt*self.dirx/tamanho)
        if self.bullet.getY() < self.initialpos[1]+256:    
            self.bullet.setY(self.bullet.getY()-40*dt*self.diry/tamanho)
    #    self.bullet.setZ(self.bullet.getZ()+0.01)