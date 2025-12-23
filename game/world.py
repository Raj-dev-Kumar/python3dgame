from panda3d.core import CardMaker, CollisionNode, CollisionSphere, TextureStage, Texture
import system
import const
from maps.begining import begining

class MapInfo:
    def __init__(self, map_id, map_class):
        self.id = map_id
        self.map_class = map_class



LISTMAPS = {
    "begining": MapInfo(1, begining)
   # "forest": MapInfo(2, forest_map)
}

class World:
    def __init__( self, render,loader, curMAP):
        map_info = LISTMAPS[curMAP]
        self.map = map_info.map_class(render,loader)