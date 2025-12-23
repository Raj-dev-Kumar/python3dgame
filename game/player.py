import math
from inventory import Inventory
import system
from panda3d.core import ClockObject
import const

class Player:
    def __init__(self, base, render, loader):
        self.node = loader.loadModel(system.get_model_path("cube_transparent_artistic_reference.glb"))
        self.node.reparentTo(render)
        self.node.setScale(1)
        self.node.setPos(96, 0, const.MIN_Z_POSITION)
        self.inventory = Inventory(base) # each Player should have a player
        self.time_jump = 0
        self.time = 0
        self.isJumpingTime = 0

        self.speed = 5

    def isOutMap(self):
        if self.node.getX() > 50 or self.node.getX() < -50 or self.node.getY() > 50 or self.node.getX() < -50:  
            return True
        return False  

    def update(self, dt, keys, yaw,frametime):
        self.time = frametime
        move = self.speed * dt
        rad_yaw = math.radians(yaw)
        cam_forward_x = math.sin(rad_yaw)
        cam_forward_y = -math.cos(rad_yaw)
        cam_right_x = math.cos(rad_yaw)
        cam_right_y = math.sin(rad_yaw)

        if self.node.getZ() >const.MIN_Z_POSITION:
            self.node.setZ(self.node.getZ()-const.FALL_SPEED*dt)

        if self.node.getZ() <const.MIN_Z_POSITION:
            self.node.setZ(const.MIN_Z_POSITION)  

        print(f" time_jump {self.time_jump} time {self.time}")   


        if  self.isJumpingTime>self.time:
            self.node.setZ(self.node,(self.node.getZ()+const.JUMP_SPEED)*dt)


        if keys[const.MOVE_BACKWARDS_KEY]:
            self.node.setX(self.node, cam_forward_x * move)
            self.node.setY(self.node, cam_forward_y * move)


        if keys[const.MOVE_FORWARD_KEY]:
            self.node.setX(self.node, -cam_forward_x * move)
            self.node.setY(self.node, -cam_forward_y * move)


        if keys[const.MOVE_LEFT_KEY]:
            self.node.setX(self.node, -cam_right_x * move)
            self.node.setY(self.node, -cam_right_y * move)

        if keys[const.MOVE_RIGHT_KEY]:
            self.node.setX(self.node, cam_right_x * move)
            self.node.setY(self.node, cam_right_y * move)
            
        if( keys[const.JUMP_KEY] and
            self.node.getZ() == const.MIN_Z_POSITION and
            self.time_jump<self.time):

            self.time_jump = self.time + const.JUMP_TIME
            self.isJumpingTime =  self.time + const.JUMP_TIME


        if self.isOutMap():
            print("Saiu do mapa")    
