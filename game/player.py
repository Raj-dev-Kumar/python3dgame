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

    def update(self, dt, keys):
        move = self.speed * dt

        if keys["w"]:
            self.node.setY(self.node, move)
        if keys["s"]:
            self.node.setY(self.node, -move)
        if keys["a"]:
            self.node.setX(self.node, -move)
        if keys["d"]:
            self.node.setX(self.node, move)
