from panda3d.core import BitMask32, CardMaker, CollisionNode, CollisionSphere, TextureStage, Texture
from panda3d.core import GeoMipTerrain
import system
class begining:
    def __init__( self, render,loader,tree_tuple):

    
        self.MAP_SIZE = 256
        self.HEIGHT_SCALE = 10

       
        self.terrain = GeoMipTerrain("terrain")
        self.terrain.setHeightfield(system.get_texture_path("../heightmap.png"))

        self.terrain.setBlockSize(32)
        self.terrain.setNear(50)
        self.terrain.setFar(200)
        self.terrain.setFocalPoint(render)

        self.terrain_root = self.terrain.getRoot()
        self.terrain_root.reparentTo(render)

        # Scale defines size
        self.terrain_root.setScale(
            1,                      # X size
            1,                      # Y size
            self.HEIGHT_SCALE       # Z height
        )

        # Center terrain at (0, 0, 0)
        self.terrain_root.setPos(
            -self.MAP_SIZE / 2,
            -self.MAP_SIZE / 2,
            0
        )

        self.terrain.generate()

        grass = loader.loadTexture(system.get_texture_path("grass_baseColor.jpeg"))
        grass.setMinfilter(Texture.FTLinearMipmapLinear)
        grass.setMagfilter(Texture.FTLinear)
        grass.setAnisotropicDegree(8)

        ts = TextureStage("grass")
        self.terrain_root.setTexture(ts, grass)
        self.terrain_root.setTexScale(ts, 256, 256)


        for i in tree_tuple:
            self.tree_model = loader.loadModel(system.get_model_path("maple_tree.glb"))
            self.TreeCollisionNode = CollisionNode("colNode")
            self.TreeCollisionNode.addSolid(CollisionSphere(0,0,0,1.5))
            self.TreeCollisionpath = self.tree_model.attachNewNode(self.TreeCollisionNode)
            self.TreeCollisionpath.show()        
            self.TreeCollisionNode.setIntoCollideMask(BitMask32.bit(1))
            self.tree_model.reparentTo(render)
            self.tree_model.setPos(i[0], i[1], i[2])
            self.tree_model.setScale(0.01)
            self.tree_model.setH(45)  # Rotate tree for variation
        # self.tree_model.attachNewNode(CollisionNode('colNode'))