import math
from panda3d.core import Vec3, WindowProperties

class CameraController:
    def __init__(self, camera, player, base):
        self.camera = camera
        self.player = player
        self.base = base

        self.distance = 15
        self.height = 8
        self.yaw = 0
        self.pitch = 20
        self.sensitivity = 0.2

        # Zoom limits
        self.min_distance = 5
        self.max_distance = 50
        self.zoom_step = 2     # how much to zoom per wheel tick        

        self.right_mouse_down = False
        self.first_frame = True

        base.accept("mouse3", self.start_rotate)
        base.accept("mouse3-up", self.stop_rotate)
        base.accept("wheel_up", self.zoom_in)
        base.accept("wheel_down", self.zoom_out)

        # Add camera update as task
        base.taskMgr.add(self.camera_task, "cameraTask")

    def zoom_in(self):
        self.distance = max(self.min_distance, self.distance - self.zoom_step)

    def zoom_out(self):
        self.distance = min(self.max_distance, self.distance + self.zoom_step)

    def start_rotate(self):
        self.right_mouse_down = True
        # Hide cursor
        props = WindowProperties()
        props.setCursorHidden(True)
        self.base.win.requestProperties(props)
        self.first_frame = True  # reset first-frame flag

    def stop_rotate(self):
        self.right_mouse_down = False
        # Show cursor
        props = WindowProperties()
        props.setCursorHidden(False)
        self.base.win.requestProperties(props)

    def camera_task(self, task):
        props = self.base.win.getProperties()
        center_x = int(props.getXSize() / 2)
        center_y = int(props.getYSize() / 2)

        md = self.base.win.getPointer(0)
        dx = md.getX() - center_x
        dy = md.getY() - center_y

        if self.right_mouse_down:
            if self.first_frame:
                # Prevent huge jump on first frame
                dx, dy = 0, 0
                self.first_frame = False

            # Update angles
            self.yaw   -= dx * self.sensitivity
            self.pitch += dy * self.sensitivity
            self.pitch = max(-10, min(60, self.pitch))

            # Recenter mouse
            self.base.win.movePointer(0, center_x, center_y)

        # Update camera position relative to player
        rad_yaw = math.radians(self.yaw)
        rad_pitch = math.radians(self.pitch)

        x = self.distance * math.sin(rad_yaw) * math.cos(rad_pitch)
        y = -self.distance * math.cos(rad_yaw) * math.cos(rad_pitch)
        z = self.height + self.distance * math.sin(rad_pitch)

        player_pos = self.player.node.getPos()
        self.camera.setPos(player_pos + Vec3(x, y, z))
        self.camera.lookAt(player_pos)

        return task.cont
