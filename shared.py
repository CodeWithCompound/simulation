
from dataclasses import dataclass
from typing import NamedTuple


class Vec2(NamedTuple):
    x: float
    y: float

COLORS = [
    "red",
    "green",
    "blue",
    "yellow",
    "magenta",
    "cyan",
    "orange",
    "white",
    "black",
]

@dataclass
class Game:
    window_size: Vec2
    world_size: Vec2
    version: str = "0.0.1"

game: Game = Game(Vec2(1000, 700), Vec2(5000, 5000))
