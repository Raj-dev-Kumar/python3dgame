from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight, CollisionNode, CollisionSphere,CollisionHandlerQueue,CollisionRay,CollisionTraverser
from panda3d.core import ClockObject,TransparencyAttrib, BitMask32
from direct.gui.DirectGui import DirectFrame,DirectButton

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

        self.world = World(self.render,self.loader,"begining")
        self.player = Player(self, self.render, self.loader)
        self.input = InputHandler(self)
        self.camera_controller = CameraController(self.camera, self.player,self)

        self.game_paused = False

        #Collision
        self.playerCollisionNode = CollisionNode("PlayerCollision")
        self.playerCollisionNode.addSolid(CollisionSphere(0,0,0,1.5))
        self.playerCollisionNode.setFromCollideMask(BitMask32.bit(1))
        self.playerCollisionpath = self.player.node.attachNewNode(self.playerCollisionNode)
        self.playerCollisionpath.show()

        self.traverser = CollisionTraverser()
        self.handler = CollisionHandlerQueue()

        self.traverser.addCollider(self.playerCollisionpath,self.handler)

        # Menu
        self.menu = GameMenu(self)
        #self.inventory = Inventory(self)

        self.player.inventory.add_item("Sword")
        self.player.inventory.add_item("Shield")

        self.ShowCoordenates()


        self.accept("escape", self.toggle_menu)

        self.taskMgr.add(self.update, "update")
        self.taskMgr.add(self.updateCol, "colisoes")

       # print(system.get_objects_by_class(self,Player))



    def updateCol(self,task):
        self.traverser.traverse(self.render)
        return task.cont



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
            self.player.update(dt, self.input.keys,self.camera_controller.yaw,globalClock.getFrameTime())
            self.ChangeCoordenates()
            if self.handler.getNumEntries() >0:
                for entry in self.handler.getEntries():
                    print(f"colidiu com {entry.getIntoNodePath().getName()}")
        else:
            if self.menu.sens_has_changed:
                 self.update_sensitivity()  
                 self.menu.sens_has_changed = False 
        #self.camera_controller.update()
        return task.cont


    def ShowCoordenates(self):
        self.positioncur = DirectFrame(
                                    frameColor=(1, 1, 1, 0.5),
                                    frameSize=(-0.4, 0.4, -0.2, 0.2),
                                    image_scale=(2, 1, 2),
                                    pos=(-0.9, 0, 0.9), 
                                    
                                 )
        
        self.positioncur.setTransparency(TransparencyAttrib.MAlpha)
        self.positioncur.show()  # Hidden by default        
        self.xcordinate = DirectButton(text=f"x:{self.player.node.getX()}",
                                       scale=0.05,
                                       pos=(-0.1, 0, 0.05),
                                       frameColor=(0, 0, 0, 0),
                                       )
        self.xcordinate.reparentTo(self.positioncur)
        self.ycordinate = DirectButton(text=f"y:{self.player.node.getY()}",
                                       scale=0.05,
                                       pos=(-0.1, 0, -0.03),
                                       frameColor=(0, 0, 0, 0),
                                       )
        self.ycordinate.reparentTo(self.positioncur)   

        self.zcordinate = DirectButton(text=f"z:{self.player.node.getZ()}",
                                       scale=0.05,
                                       pos=(-0.1, 0, -0.12),
                                       frameColor=(0, 0, 0, 0),
                                       )
        self.zcordinate.reparentTo(self.positioncur)   

    def ChangeCoordenates(self):
        self.xcordinate["text"] = f"x:{self.player.node.getX()}"            
        self.ycordinate["text"] = f"y:{self.player.node.getY()}"     
        self.zcordinate["text"] = f"z:{self.player.node.getZ()}"                  