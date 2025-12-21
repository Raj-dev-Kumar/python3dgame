from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight
from panda3d.core import ClockObject

globalClock = ClockObject.getGlobalClock()

from world import World
from player import Player
from input import InputHandler
from camera import CameraController
from menu import GameMenu
from inventory import Inventory


class Game(ShowBase):
    def __init__(self):
        super().__init__()



        self.disableMouse()

        self.setup_camera()
        self.setup_lighting()

        self.world = World(self.render)
        self.player = Player(self.render, self.loader)
        self.input = InputHandler(self)
        self.camera_controller = CameraController(self.camera, self.player,self)

        self.game_paused = False


        # Menu
        self.menu = GameMenu(self)
        self.inventory = Inventory(self)

        self.inventory.add_item("Sword")
        self.inventory.add_item("Shield")
                
        self.accept("escape", self.toggle_menu)

        self.taskMgr.add(self.update, "update")

    def setup_camera(self):
        self.camera.setPos(0, -20, 10)
        self.camera.lookAt(0, 0, 0)

    def setup_lighting(self):
        ambient = AmbientLight("ambient")
        ambient.setColor((0.4, 0.4, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        sun = DirectionalLight("sun")
        sun.setColor((0.8, 0.8, 0.8, 1))
        sun_node = self.render.attachNewNode(sun)
        sun_node.setHpr(-45, -60, 0)
        self.render.setLight(sun_node)

    def toggle_menu(self):
        if self.menu.frame.isHidden():
            self.menu.show()
        else:
            self.menu.hide()

    def update(self, task):
        if not self.game_paused:    
            dt = globalClock.getDt()
            self.player.update(dt, self.input.keys)
        #self.camera_controller.update()
        return task.cont
