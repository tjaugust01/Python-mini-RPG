import random
from type import Room, RoomType, NPC, GameConfig, Player, Item

GAME_CONFIG = GameConfig(
    rows=3,
    rooms_per_row=3,
    monster_count=0,
)

def print_intro():
    print('''
    Welcome to your own RPG Game
    ============================

    Objective 1: Get to the Garden with a key and a potion.
    Objective 2: Get to the Laboratory with the BookOfLife and Beam-O-Mat.
    Avoid the monsters!
    ''')

def print_commands():
    print('''
    Commands:
      go [direction]
      get [item]
    ''')

def init_rooms():
    """
    Erstellt ein Spielfeld (Grid).
    Sicherstellt, dass genau ein GARDEN und genau ein LABORATORY existieren.
    """
    rooms = []
    # Alle Typen außer die speziellen Ziel-Räume
    other_types = [t for t in RoomType if t not in [RoomType.GARDEN, RoomType.LABORATORY]]
    
    for x in range(GAME_CONFIG.rows):
        row = []
        for y in range(GAME_CONFIG.rooms_per_row):
            room_type = random.choice(other_types)
            row.append(Room(room_type=room_type, x=x, y=y))
        rooms.append(row)
        
    # Alle verfügbaren Koordinaten sammeln
    coords = [(x, y) for x in range(GAME_CONFIG.rows) for y in range(GAME_CONFIG.rooms_per_row)]
    random.shuffle(coords)
    
    # 1. Garten platzieren
    gx, gy = coords.pop()
    rooms[gx][gy].room_type = RoomType.GARDEN
    
    # 2. Labor platzieren
    lx, ly = coords.pop()
    rooms[lx][ly].room_type = RoomType.LABORATORY
    
    return rooms


def init_monsters(rooms, start_room):
    remaining_monster = GAME_CONFIG.monster_count
    while remaining_monster > 0:
        room = get_random_room(rooms)
        # Monster nicht im Startraum und nicht in Ziel-Räume
        if room.content is None and room != start_room and room.room_type not in [RoomType.GARDEN, RoomType.LABORATORY]:
            room.content = NPC.Monster
            remaining_monster -= 1


def init_room_content(rooms, start_room):
    # 1. Monster platzieren
    init_monsters(rooms, start_room)
    
    # 2. Alle Items platzieren
    items_to_place = [Item.Key, Item.Potion, Item.BookOfLife, Item.BeamOMat]
    for item in items_to_place:
        placed = False
        while not placed:
            room = get_random_room(rooms)
            # Bedingungen: Leer, nicht Start, kein Ziel-Raum (da man dort gewinnen muss)
            if room.content is None and room != start_room and room.room_type not in [RoomType.GARDEN, RoomType.LABORATORY]:
                room.content = item
                placed = True

def find_start_room(rooms):
    for row in rooms:
        for room in row:
            if room.room_type == RoomType.HALL:
                return room
    return rooms[0][0]

def get_random_room(rooms):
    row = random.choice(rooms)
    room = random.choice(row)
    return room

def show_status(current_room, inventory):
    print('---------------------------')
    print('You are in the ' + current_room.name)
    print('Inventory : ' + str(inventory))
    if current_room.content is not None:
        content_name = current_room.content.value if hasattr(current_room.content, 'value') else str(current_room.content)
        print('You see a ' + content_name)
    print('---------------------------')

def configure_game_settings():
    print('Game Settings:')
    print('Rows: ' + str(GAME_CONFIG.rows))
    print('Rooms per Row: ' + str(GAME_CONFIG.rooms_per_row))
    print('Monster Count: ' + str(GAME_CONFIG.monster_count))
    print('Do you want to change the settings? (y/n):')
    response = input().lower()
    if response == 'y':
        GAME_CONFIG.rows = int(input('Rows: '))
        GAME_CONFIG.rooms_per_row = int(input('Rooms per Row: '))
        GAME_CONFIG.monster_count = int(input('Monster Count: '))


def check_win_condition(player: Player, rooms: list[list[Room]]):
    current_room = player.get_current_room(rooms)
    
    # Bedingung 1: Garten + Key + Potion
    if current_room.room_type == RoomType.GARDEN and player.has_key() and player.has_potions():
        print("Victory! You reached the garden with the key and potion!")
        return True
    
    # Bedingung 2: Laboratory + BookOfLife + BeamOMat
    if current_room.room_type == RoomType.LABORATORY and player.has_book() and player.has_beamomat():
        print("Victory! You reached the laboratory with the Book of Life and Beam-O-Mat!")
        return True
        
    return False


def game_loop(player: Player, rooms: list[list[Room]]):
    while True:
        current_room = player.get_current_room(rooms)
        show_status(current_room, player.inventory)
        
        if current_room.content == NPC.Monster:
            print("A Monster has eaten you! GAME OVER")
            break
            
        if check_win_condition(player, rooms):
            break
            
        command(player, rooms)


def move_player(player, param, rooms: list[list[Room]]):
    match param.lower():
        case "up" | "north" | "w": player.move_up(rooms)
        case "down" | "south" | "s": player.move_down(rooms)
        case "left" | "west" | "a": player.move_left(rooms)
        case "right" | "east" | "d": player.move_right(rooms)
        case _: print("Invalid direction")


def get_item(player, param, rooms: list[list[Room]]):
    current_room = player.get_current_room(rooms)
    item_in_room = current_room.content
    if item_in_room is None or isinstance(item_in_room, NPC):
        print("There is nothing here to pick up.")
        return
    if param.lower() == item_in_room.value.lower():
        player.inventory.append(item_in_room.value)
        current_room.content = None
        print("You got the " + item_in_room.value)
    else:
        print("No " + param + " in this room")


def command(player: Player, rooms: list[list[Room]]):
    user_input = input("> ").lower().split()
    if not user_input: return
    match user_input:
        case ["go", direction]: move_player(player, direction, rooms)
        case ["get", item]: get_item(player, item, rooms)
        case _: print("Invalid command.")
