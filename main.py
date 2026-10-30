
import pygame
from camera import Camera
from entity_setup import make_entity
from environment import TreeManager
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

    tree_manager = TreeManager()
    tree_manager.init_tree_spawn(game.world_size) # Spawns 700 trees in the world

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
        screen.fill("brown")
        for tree in tree_manager.trees:
            sx, sy = cam.world_to_screen(tree.pos.x, tree.pos.y)
            w = int(tree.surface.get_width() * cam.zoom)
            h = int(tree.surface.get_height() * cam.zoom)
            # Simple culling: Only draw if it's roughly on screen
            if -w < sx < cam.screen_w + w and -h < sy < cam.screen_h + h:
                # Scale the surface
                scaled_tree = pygame.transform.scale(tree.surface, (w, h))
                # Get the rect and center it at the screen position
                tree_rect = scaled_tree.get_rect(center=(sx, sy))

                screen.blit(scaled_tree, tree_rect)

        for e in entities:
            e.draw(screen, cam)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
