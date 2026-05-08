from dataclasses import dataclass
from enum import Enum


class RoomType(Enum):
    HALL = "Hallway"
    KITCHEN = "Kitchen"
    GARDEN = "Garden"
    LIBRARY = "Library"
    OFFICE = "Office"
    LABORATORY = "Laboratory"

class NPC(Enum):
    Monster = "Monster"

class Item(Enum):
    Potion = "Potion"
    Key = "Key"
    Chopsticks = "Chopsticks"
    BookOfLife = "BookOfLife"
    BeamOMat = "Beam-O-Mat"

@dataclass
class Room:
    room_type: RoomType
    x: int
    y: int
    content: Item|NPC|None = None

    @property
    def name(self):
        return self.room_type.value

@dataclass
class Player:
    x: int
    y: int
    inventory: list[str]

    def get_current_room(self, rooms: list[list[Room]]) -> Room:
        return rooms[self.x][self.y]

    def has_potions(self) -> bool:
        return Item.Potion.value in self.inventory

    def has_key(self) -> bool:
        return Item.Key.value in self.inventory
    
    def has_book(self) -> bool:
        return Item.BookOfLife.value in self.inventory
        
    def has_beamomat(self) -> bool:
        return Item.BeamOMat.value in self.inventory

    def move_up(self, rooms: list[list[Room]]):
        if self.x > 0:
            self.x -= 1
        else:
            print("You hit a wall! You can't go further north.")

    def move_down(self, rooms: list[list[Room]]):
        if self.x < len(rooms) - 1:
            self.x += 1
        else:
            print("You hit a wall! You can't go further south.")

    def move_left(self, rooms: list[list[Room]]):
        if self.y > 0:
            self.y -= 1
        else:
            print("You hit a wall! You can't go further west.")

    def move_right(self, rooms: list[list[Room]]):
        if self.y < len(rooms[0]) - 1:
            self.y += 1
        else:
            print("You hit a wall! You can't go further east.")

@dataclass()
class GameConfig:
    rows: int = 3
    rooms_per_row: int = 3
    monster_count: int = 2