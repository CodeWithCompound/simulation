class Camera:
    def __init__(self, world_w, world_h, screen_w, screen_h):
        self.x = 0.0
        self.y = 0.0
        self.zoom = 1.0
        self.world_w = world_w
        self.world_h = world_h
        self.screen_w = screen_w
        self.screen_h = screen_h

    def world_to_screen(self, wx, wy):
        return (int((wx - self.x) * self.zoom),
                int((wy - self.y) * self.zoom))

    def clamp(self):
        vw = self.screen_w / self.zoom
        vh = self.screen_h / self.zoom
        self.x = max(0.0, min(self.x, self.world_w - vw))
        self.y = max(0.0, min(self.y, self.world_h - vh))
