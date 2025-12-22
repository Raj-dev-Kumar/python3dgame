import os
import sys
from panda3d.core import Filename
import const

# Base folder of the project (assuming this file is inside a 'game' folder)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_DIR = os.path.join(BASE_DIR, const.ASSETS_DIR_NAME)

def is_frozen():
    return getattr(sys, const.STATE_FROZEN, False)

def get_asset_path(filename: str) -> Filename:
    """
    Returns a Panda3D-friendly Filename object for any asset inside the assets folder.
    
    Usage:
        tex_path = get_asset_path("menu.png")
        loader.loadTexture(tex_path)
    """
    full_path = os.path.join(ASSETS_DIR, filename)
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"Asset not found: {full_path}")
    return Filename.fromOsSpecific(full_path)

def get_model_path(filename: str) -> Filename:
    """
    Returns a Panda3D-friendly Filename object for a model file inside assets/models.
    """
    if const.GLB_EXTENSION in filename and is_frozen():
        filename = filename + const.BAM_EXTENSION
    models_dir = os.path.join(ASSETS_DIR, const.MODELS_DIR_NAME)
    full_path = os.path.join(models_dir, filename)
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"Model not found: {full_path}")
    return Filename.fromOsSpecific(full_path)

def get_objects_by_class(obj, cls):
    return [
        value
        for value in vars(obj).values()
        if isinstance(value, cls)
    ]

def get_texture_path(filename: str) -> Filename:
    """
    Returns a Panda3D-friendly Filename object for any asset inside the assets folder.
    
    Usage:
        tex_path = get_asset_path("menu.png")
        loader.loadTexture(tex_path)
    """
    TEXTURE_PATH = os.path.join(ASSETS_DIR, "textures")
    full_path = os.path.join(TEXTURE_PATH, filename)
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"Asset not found: {full_path}")
    return Filename.fromOsSpecific(full_path)