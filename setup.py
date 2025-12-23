from setuptools import setup

setup(
    name="python3dgame",
    version="0.2",
    description="A 3D game",
    author="RajdevKumar",

    options={
        "build_apps": {
            # Build your GUI app
            "gui_apps": {
                "python3dgame": "game/main.py",  # exe name : entry script
            },
            "icons":
               {
                    # The key needs to match the key used in gui_apps/console_apps.
                    # Alternatively, use "*" to set the icon for all apps.
                    "python3dgame": ["icon.ico","icon.png","icon.png","icon.png","icon.png"],
                },
            # Include assets like textures, models, and other folders
            "include_patterns": [
                "assets/**/*",
            ],
            # Panda3D plugins to include in the build
            "plugins": [
                "pandagl",          # OpenGL renderer
                "p3openal_audio",    # Audio backend

            ],
            "bam_model_extensions": ["gltf", "glb"],
            'platforms':['win_amd64'],
            "include_modules": ["panda3d_gltf"],
            # Optional: log file for debugging runtime issues
            "log_filename": "$USER_APPDATA/python3dgame/output.log",
            "log_append": True,
        },
    },

    install_requires=[
        "Panda3D==1.10.15",
        "panda3d-gltf==1.3.0",
        "panda3d-simplepbr==0.13.1"
    ],
)
