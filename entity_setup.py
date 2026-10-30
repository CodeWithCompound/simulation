import random
from dataclasses import dataclass

import pygame
from shared import COLORS, Vec2


@dataclass
class Entity:
    pos: Vec2
    color: str
    verlocity: Vec2
    radius: float = 7

    def draw(self, screen, cam):
        sx, sy = cam.world_to_screen(self.pos.x, self.pos.y)
        r = max(1, int(self.radius * cam.zoom))
        # cull offscreen entities
        if -r < sx < cam.screen_w + r and -r < sy < cam.screen_h + r:
            pygame.draw.circle(screen, self.color, (sx, sy), r)

    def update_position(self, dt, world_size):
        r = self.radius
        vx, vy = self.verlocity
        x = self.pos.x + vx * dt
        y = self.pos.y + vy * dt

        if x - r <= 0:
            x, vx = r, -vx
        elif x + r >= world_size.x:
            x, vx = world_size.x - r, -vx

        if y - r <= 0:
            y, vy = r, -vy
        elif y + r >= world_size.y:
            y, vy = world_size.y - r, -vy

        self.pos = Vec2(x, y)
        self.verlocity = Vec2(vx, vy)

    def update(self, dt, world_size):
        self.update_position(dt, world_size)


def make_entity(world_size):
    return Entity(
        pos=Vec2(random.uniform(0, world_size.x),
                 random.uniform(0, world_size.y)),
        verlocity=Vec2(random.uniform(-100, 100),
                       random.uniform(-100, 100)),
        color=random.choice(COLORS),
    )
