class Player:
    def __init__(self, render, loader):
        self.node = loader.loadModel("models/box")
        self.node.reparentTo(render)
        self.node.setScale(1)
        self.node.setPos(0, 0, 1)

        self.speed = 5

    def update(self, dt, keys):
        move = self.speed * dt

        if keys["w"]:
            self.node.setY(self.node, move)
        if keys["s"]:
            self.node.setY(self.node, -move)
        if keys["a"]:
            self.node.setX(self.node, -move)
        if keys["d"]:
            self.node.setX(self.node, move)
