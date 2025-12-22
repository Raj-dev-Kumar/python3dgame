from panda3d.core import CardMaker, CollisionNode, CollisionSphere, TextureStage, Texture
import system
class World:
    def __init__( self, render,loader):
        ground = CardMaker("ground")
        ground.setFrame(-50, 50, -50, 50)
        

        node = render.attachNewNode(ground.generate())
        node.setP(-90)
        node.setZ(0)


        ground_tex = loader.loadTexture(system.get_texture_path("grass_baseColor.jpeg"))
        ground_tex.setMinfilter(Texture.FTLinearMipmapLinear)
        ground_tex.setMagfilter(Texture.FTLinear)
        ground_tex.setAnisotropicDegree(8)
        # Apply texture
        ts_grass = TextureStage("grass")
        node.setTexture(ts_grass, ground_tex)
        node.setTexScale(ts_grass, 20, 20)



                # DIRT PATCH
        dirt = CardMaker("dirt")
        dirt.setFrame(-50, 10, -10,-40)
        dirt_np = render.attachNewNode(dirt.generate())
        dirt_np.setP(-90.01)
        dirt_np.setZ(0)  # Slightly higher to avoid z-fighting

        dirt_tex = loader.loadTexture(system.get_texture_path("grass_metallicRoughness.png"))
        dirt_tex.setMinfilter(Texture.FTLinearMipmapLinear)
        dirt_tex.setMagfilter(Texture.FTLinear)
        dirt_tex.setAnisotropicDegree(8)        
        ts_dirt = TextureStage("dirt")
        dirt_np.setTexture(ts_dirt, dirt_tex)
        dirt_np.setTexScale(ts_dirt, 4, 4)


        self.tree_model = loader.loadModel(system.get_model_path("maple_tree.glb"))
        self.tree_model.reparentTo(render)
        self.tree_model.setPos(10, 10, 0)
        self.tree_model.setScale(0.01)
        self.tree_model.setH(45)  # Rotate tree for variation
        self.tree_model.attachNewNode(CollisionNode('colNode'))