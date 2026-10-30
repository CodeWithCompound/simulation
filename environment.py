import pygame


def load_tree_sprite() -> list[pygame.Surface]:
    sprite_sheet = pygame.image.load("assets/16x32 trees.png").convert_alpha()

    # Dimensions
    TREE_WIDTH = 16
    TREE_HEIGHT = 32
    COLUMNS = 4
    ROWS = 2

    trees: list[pygame.Surface] = []
    for row in range(ROWS):
        for col in range(COLUMNS):
            # Calculate the top-left coordinates for the current tree
            x = col * TREE_WIDTH
            y = row * TREE_HEIGHT

            # Create a new empty surface with transparency
            tree_surface = pygame.Surface((TREE_WIDTH, TREE_HEIGHT), pygame.SRCALPHA)

            # Blit (copy) just that specific 16x32 area from the sprite sheet
            tree_surface.blit(sprite_sheet, (0, 0), (x, y, TREE_WIDTH, TREE_HEIGHT))

            # Add it to our list
            trees.append(tree_surface)

    print(f"Loaded {len(trees)} trees!")
    return trees
