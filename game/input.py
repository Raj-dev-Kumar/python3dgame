import const

class InputHandler:
    def __init__(self, base):
        self.keys = {
                    const.MOVE_FORWARD_KEY: False,
                    const.MOVE_LEFT_KEY: False,
                    const.MOVE_BACKWARDS_KEY: False,
                    const.MOVE_RIGHT_KEY: False,
                    const.JUMP_KEY:False,
                    const.MOUSE_LEFT:False
                    }

        for key in self.keys:
            base.accept(key, self.set_key, [key, True])
            base.accept(f"{key}-up", self.set_key, [key, False])

    def set_key(self, key, value):
        self.keys[key] = value
