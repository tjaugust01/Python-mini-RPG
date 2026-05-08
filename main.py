from util import print_intro, print_commands, init_rooms, init_room_content, show_status, find_start_room, GAME_CONFIG, \
    configure_game_settings, game_loop
from type import Player

def game():
    while True:
        print_intro()
        print_commands()
        configure_game_settings()
        rooms = init_rooms()

        # 1. Startraum finden (Anforderung: Halle)
        start_room = find_start_room(rooms)

        # 2. Initialisiere Spieler am Startraum
        player = Player(x=start_room.x, y=start_room.y, inventory=[])

        print('''
        Aktuelles Raum-Grid:
        ''')

        for row in rooms:
            room_names = []
            for room in row:
                if room == start_room:
                    room_names.append(f'[{room.name}]')
                else:
                    room_names.append(room.name)

            print(" | ".join(room_names))

        # 3. Loot/Monster initialisieren (Startraum ausschließen)
        print('Initialisiere Loot')
        init_room_content(rooms, start_room)

        game_loop(player, rooms)
        
        print("\nDo you want to play again? (y/n)")
        if input().lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    game()
