import random
from dataclasses import dataclass, field

import pygame

from shared import Vec2  # Assuming this is the correct path now


@dataclass
class EnvRules:
    max_trees: int = 700
    max_entities: int = 1000


@dataclass
class Tree:
    pos: Vec2
    surface: pygame.Surface


@dataclass
class TreeManager:
    age: float = 0.0
    food_value_and_size: float = 1.0
    init_spawn_amount: int = 700

    # We store the list of trees and sprites here
    trees: list[Tree] = field(default_factory=list)
    tree_sprites: list[pygame.Surface] = field(default_factory=list)

    def __post_init__(self):
        # Load the sprites ONCE when the manager is created
        self.tree_sprites = self.load_tree_sprite()

    def init_tree_spawn(self, worldsize: Vec2):
        for _ in range(self.init_spawn_amount):
            # Pick a random position in the world
            pos = Vec2(
                random.uniform(10.0, worldsize.x - 10.0),
                random.uniform(10.0, worldsize.y - 10.0)
            )
            self.spawn_tree(pos)

    def spawn_tree(self, pos: Vec2):
        # Pick a random sprite from our pre-loaded list
        sprite = random.choice(self.tree_sprites)
        new_tree = Tree(pos=pos, surface=sprite)
        self.trees.append(new_tree)

    def load_tree_sprite(self) -> list[pygame.Surface]:
        sprite_sheet = pygame.image.load("assets/16x32 trees.png").convert_alpha()

        TREE_WIDTH = 16
        TREE_HEIGHT = 32
        COLUMNS = 4
        ROWS = 2

        trees: list[pygame.Surface] = []
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = col * TREE_WIDTH
                y = row * TREE_HEIGHT

                tree_surface = pygame.Surface((TREE_WIDTH, TREE_HEIGHT), pygame.SRCALPHA)
                tree_surface.blit(sprite_sheet, (0, 0), (x, y, TREE_WIDTH, TREE_HEIGHT))
                trees.append(tree_surface)

        print(f"Loaded {len(trees)} tree sprites!")
        return trees
