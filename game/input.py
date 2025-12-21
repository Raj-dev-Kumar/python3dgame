class InputHandler:
    def __init__(self, base):
        self.keys = {"w": False, "a": False, "s": False, "d": False}

        for key in self.keys:
            base.accept(key, self.set_key, [key, True])
            base.accept(f"{key}-up", self.set_key, [key, False])

    def set_key(self, key, value):
        self.keys[key] = value
