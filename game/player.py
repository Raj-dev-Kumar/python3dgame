import math

from inventory import Inventory
import system
class Player:
    def __init__(self, base, render, loader):
        self.node = loader.loadModel(system.get_model_path("cube_transparent_artistic_reference.glb"))
        self.node.reparentTo(render)
        self.node.setScale(1)
        self.node.setPos(0, 0, 0)

        self.inventory = Inventory(base) # each Player should have a player

        self.speed = 5

    def isOutMap(self):
        if self.node.getX() > 50 or self.node.getX() < -50 or self.node.getY() > 50 or self.node.getX() < -50:  
            return True
        return False  

    def update(self, dt, keys, yaw):
        move = self.speed * dt
        rad_yaw = math.radians(yaw)
        cam_forward_x = math.sin(rad_yaw)
        cam_forward_y = -math.cos(rad_yaw)
        cam_right_x = math.cos(rad_yaw)
        cam_right_y = math.sin(rad_yaw)


        if keys["s"]:
            self.node.setX(self.node, cam_forward_x * move)
            self.node.setY(self.node, cam_forward_y * move)
        if keys["w"]:
            self.node.setX(self.node, -cam_forward_x * move)
            self.node.setY(self.node, -cam_forward_y * move)
        if keys["a"]:
            self.node.setX(self.node, -cam_right_x * move)
            self.node.setY(self.node, -cam_right_y * move)
        if keys["d"]:
            self.node.setX(self.node, cam_right_x * move)
            self.node.setY(self.node, cam_right_y * move)

        if self.isOutMap():
            print("Saiu do mapa")    
