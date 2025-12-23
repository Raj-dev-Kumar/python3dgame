from panda3d.core import CardMaker, CollisionNode, CollisionSphere, TextureStage, Texture
import system
import const
from maps.begining import begining

class MapInfo:
    def __init__(self, map_id, map_class, tree_tuple):
        self.id = map_id
        self.map_class = map_class
        self.tree_tuple = tree_tuple



LISTMAPS = {
    "begining": MapInfo(1, begining,
                        (
                         (96,1,0),
                         (95,6,0)
                        )
                         )
   # "forest": MapInfo(2, forest_map)
}

class World:
    def __init__( self, render,loader, curMAP):
        map_info = LISTMAPS[curMAP]
        self.map = map_info.map_class(render,loader,map_info.tree_tuple)