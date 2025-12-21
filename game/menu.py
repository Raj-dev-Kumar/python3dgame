from direct.gui.DirectGui import DirectFrame, DirectButton
from panda3d.core import TransparencyAttrib
import system

class GameMenu:
    def __init__(self, base):
        self.base = base
        self.bg_tex = self.base.loader.loadTexture(system.get_asset_path("menu.jpeg"))
        self.frame = DirectFrame(
                                    frameColor=(1, 1, 1, 1),
                                    frameSize=(-1, 1, -1, 1),
                                    image_scale=(2, 1, 2),
                                    
                                 )
        self.frame.setTransparency(TransparencyAttrib.MAlpha)
        self.frame.setTexture(self.bg_tex)
        self.frame.hide()  # Hidden by default

        self.resume_btn = DirectButton(text="Resume",
                                       scale=0.08,
                                       pos=(0, 0, 0.2),
                                       command=self.hide)
        self.resume_btn.reparentTo(self.frame)

        self.quit_btn = DirectButton(text="Quit",
                                     scale=0.08,
                                     pos=(0, 0, -0.2),
                                     command=self.quit_game)
        self.quit_btn.reparentTo(self.frame)

    def show(self):
        self.frame.show()
        self.base.game_paused = True  # Pause game updates

    def hide(self):
        self.frame.hide()
        self.base.game_paused = False  # Resume game updates

    def quit_game(self):
        self.base.userExit()
