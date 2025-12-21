from panda3d.core import CardMaker
import system
class World:
    def __init__( self, render,loader):
        ground = CardMaker("ground")
        ground.setFrame(-50, 50, -50, 50)
        

        node = render.attachNewNode(ground.generate())
        node.setP(-90)
        node.setZ(0)
        tree_model = loader.loadModel(system.get_model_path("maple_tree.glb"))
        tree_model.reparentTo(render)
        tree_model.setPos(10, 10, 0)
        tree_model.setScale(0.01)
        tree_model.setH(45)  # Rotate tree for variation