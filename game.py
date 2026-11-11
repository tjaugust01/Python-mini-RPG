import os
import pprint
import pygame

from type import NPC, Player, Room, RoomType
from util import check_win_condition, find_start_room, init_room_content, init_rooms

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400,300))
        self.bg_color = (30,30,30)
        self.field_x_size = 90
        self.field_y_size = 90
        self.field_size = [self.field_x_size,self.field_y_size]
        self.images = {}
        self.load_assets()
        self.rooms = init_rooms()
        pygame.font.init()

    def draw_base_board(self):
        self.screen.fill(self.bg_color)
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 300, 200), 2)

    def draw_all_rooms(self):
        y_cord = 0
        for row in self.rooms:
            x_cord = 0
            for room in row:
                self.draw_field(room, x_cord, y_cord)
                x_cord += self.field_x_size
            y_cord += self.field_y_size

    def draw_field(self, room: Room, x, y):
        self.screen.blit(self.images[room.room_type], (x, y))

    def load_assets(self):
        for room_type in RoomType:
            filename = f"{room_type.value}.png"
            path = os.path.join("sprites", filename)
            
            try:
                img = pygame.image.load(path).convert_alpha()
                self.images[room_type] = pygame.transform.scale(img, self.field_size)
            except pygame.error:
                print(f"⚠️ Konnte Asset nicht finden: {path}")
                fallback = pygame.Surface(self.field_size)
                fallback.fill((255, 0, 255))
                self.images[room_type] = fallback

        try:
            self.player_img = pygame.image.load("sprites/player.png").convert_alpha()
            self.player_img = pygame.transform.scale(self.player_img, (64, 64))
        except pygame.error:
            print("⚠️ Spieler-Sprite fehlt!")

    def load_player(self):
        start_room = find_start_room(self.rooms)
        self.player = Player(x=start_room.x, y=start_room.y, inventory=[])

    def handle_get_item(self):
        current_room = self.player.get_current_room(self.rooms)
        item_in_room = current_room.content
        if item_in_room is None or isinstance(item_in_room, NPC):
            print("There is nothing here to pick up.")
            return
        
        self.player.inventory.append(item_in_room.value)
        current_room.content = None
        print("You got the " + item_in_room.value)

    def show_end_screen(self, image_path):
        try:
            img = pygame.image.load(image_path).convert_alpha()
            img = pygame.transform.scale(img, (400, 300))
            self.screen.blit(img, (0, 0))
            pygame.display.flip()
            pygame.time.delay(3000)
        except pygame.error:
            print(f"⚠️ End-Screen fehlt: {image_path}")

    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                        
            if event.type == pygame.KEYDOWN:
                # W -> HOCH (y verringern)
                if event.key == pygame.K_w: 
                    self.player.move_up(self.rooms)
                
                # S -> RUNTER (y erhöhen)
                if event.key == pygame.K_s: 
                    self.player.move_down(self.rooms)
                
                # A -> LINKS (x verringern)
                if event.key == pygame.K_a: 
                    self.player.move_left(self.rooms)
                
                # D -> RECHTS (x erhöhen)
                if event.key == pygame.K_d: 
                    self.player.move_right(self.rooms)
                
                # E -> AUFHEBEN
                if event.key == pygame.K_e:
                    self.handle_get_item()
        return True

    def run(self):
        pprint.pprint(self.rooms)
        self.load_player()
        
        start_room = self.player.get_current_room(self.rooms)
        
        print('Initialisiere Loot')
        init_room_content(self.rooms, start_room)
        
        running = True
        while running:
            # 1. Steuerung
            running = self.play()
            if not running:
                break

            # 2. Logik
            current_room = self.player.get_current_room(self.rooms)
            
            if current_room.content == NPC.Monster:
                self.show_end_screen("sprites/merz.png")
                self.show_end_screen("sprites/lose.png")
                break
                
            if check_win_condition(self.player, self.rooms):
                self.show_end_screen("sprites/win.png")
                break

            # 3. Zeichnen
            self.draw_base_board()
            self.draw_all_rooms()
            
            # Spieler zeichnen (zentriert im Feld)
            self.screen.blit(self.player_img, (self.player.x * self.field_x_size + 13, self.player.y * self.field_y_size + 13))

            # Item visuell im Raum andeuten
            if current_room.content is not None and not isinstance(current_room.content, NPC):
                font = pygame.font.SysFont("Arial", 16)
                text = font.render(f"E: {current_room.content.value}", True, (255, 255, 0))
                self.screen.blit(text, (self.player.x * self.field_x_size + 5, self.player.y * self.field_y_size + 5))

            pygame.display.flip()
            
        pygame.quit()