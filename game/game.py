from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight, CollisionNode, CollisionSphere,CollisionHandlerPusher,CollisionRay
from panda3d.core import ClockObject

globalClock = ClockObject.getGlobalClock() # glock used by the pandas used for deltatime beetwen frame

from world import World
from player import Player
from input import InputHandler
from camera import CameraController
from menu import GameMenu
from inventory import Inventory
import system


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        """
        super().__init__(), starts the ShowBase class which is responsible for window rendering
                            starts the render and creates the task manager(taskMgr)
                            Handles input
                            Initializes Cameras

        Render - Everything that is displayed by 3D world need to be atached to the scene Graph
                 which is handled by the render.
                 This is what adds the player to the world.
                 creates the world, etc

        task manager(taskMgr) - executes tasks every frame, 
                                updates object position,
                                animations and game logic         
        
        """
        


        self.disableMouse() # to use costume Mouse

        self.setup_camera()
        self.setup_lighting()

        self.world = World(self.render,self.loader)
        self.player = Player(self, self.render, self.loader)
        self.input = InputHandler(self)
        self.camera_controller = CameraController(self.camera, self.player,self)

        self.game_paused = False
   

        # Menu
        self.menu = GameMenu(self)
        #self.inventory = Inventory(self)

        self.player.inventory.add_item("Sword")
        self.player.inventory.add_item("Shield")

        self.accept("escape", self.toggle_menu)

        self.taskMgr.add(self.update, "update")

       # print(system.get_objects_by_class(self,Player))

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
            

    def update_sensitivity(self):
        # Get current slider value
        new_sensitivity = self.menu.sensitivityBar['value']  
        self.camera_controller.SetSensivity(new_sensitivity)         

    def update(self, task):
        if not self.game_paused:    
            dt = globalClock.getDt()
            self.player.update(dt, self.input.keys,self.camera_controller.yaw)
        else:
            if self.menu.sens_has_changed:
                 self.update_sensitivity()  
                 self.menu.sens_has_changed = False 
        #self.camera_controller.update()
        return task.cont
