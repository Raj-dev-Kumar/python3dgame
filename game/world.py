from panda3d.core import CardMaker

class World:
    def __init__(self, render):
        ground = CardMaker("ground")
        ground.setFrame(-50, 50, -50, 50)

        node = render.attachNewNode(ground.generate())
        node.setP(-90)
        node.setZ(0)
