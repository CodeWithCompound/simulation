import pygame
from camera import Camera
from entity_setup import make_entity
from environment import load_tree_sprite
from shared import game


def main():
    pygame.init()
    screen = pygame.display.set_mode(game.window_size)
    clock = pygame.time.Clock()

    cam = Camera(game.world_size.x, game.world_size.y,
                 game.window_size.x, game.window_size.y)

    target = [0.0, 0.0]
    speed = 2000.0

    entities = [make_entity(game.world_size) for _ in range(1500)]
    load_tree_sprite()

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                mx, my = pygame.mouse.get_pos()
                before = (cam.x + mx / cam.zoom, cam.y + my / cam.zoom)
                cam.zoom = max(0.25, min(4.0, cam.zoom * (1.1 ** event.y)))
                cam.x = before[0] - mx / cam.zoom
                cam.y = before[1] - my / cam.zoom

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  target[0] -= speed * dt / cam.zoom
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: target[0] += speed * dt / cam.zoom
        if keys[pygame.K_w] or keys[pygame.K_UP]:    target[1] -= speed * dt / cam.zoom
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  target[1] += speed * dt / cam.zoom

        cam.x += (target[0] - cam.x) * 0.15
        cam.y += (target[1] - cam.y) * 0.15
        cam.clamp()
        target[0], target[1] = cam.x, cam.y

        # --- Update ---
        for e in entities:
            e.update(dt, game.world_size)

        # --- Draw ---
        screen.fill("purple")
        for e in entities:
            e.draw(screen, cam)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
