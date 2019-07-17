import pygame
import random 
import time
from constants import RED, YELLOW, BLUE, GREEN, FPS, WIDTH, HEIGHT








 



class Backdrop(pygame.sprite.Sprite):
    """The backdrop image for the game"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/backgrounds/start_page.jpg")

        self.rect = self.image.get_rect()
        self.rect.w


class ColorBox(pygame.sprite.Sprite):
    def __init__(self, color, selected = False):
        super().__init__()
        # self.input = input_dict
        self.selected = selected
        self.color = color
        self.set_color(color)
        self.set_selected(selected)
        self.set_position()


    def set_position(self):

        if self.color == RED:
            self.rect.x = 404
            self.rect.y = 146
        elif self.color == GREEN: 
            self.rect.x = 215
            self.rect.y = 146
        elif self.color == YELLOW:
            self.rect.x = 404
            self.rect.y = 335
        elif self.color == BLUE:
            self.rect.x = 215
            self.rect.y = 335
        


    def set_color(self, color):
        if self.selected:
            if color == RED:
                self.image = pygame.image.load("assets/images/red_bright.png")
            elif color == GREEN:
                self.image = pygame.image.load("assets/images/green_bright.png")
            elif color == YELLOW:
                self.image = pygame.image.load("assets/images/yellow_bright.png")
            elif color == BLUE: 
                self.image = pygame.image.load("assets/images/blue_bright.png")
        else:
            if color == RED:
                self.image = pygame.image.load("assets/images/red_dull.png")
            elif color == GREEN:
                self.image = pygame.image.load("assets/images/green_dull.png")
            elif color == YELLOW:
                self.image = pygame.image.load("assets/images/yellow_dull.png")
            elif color == BLUE: 
                self.image = pygame.image.load("assets/images/blue_dull.png")


        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (189, 189))
        self.set_position()

    def set_selected(self, selected):
        self.selected = selected
        self.set_color(self.color)
        


    





class Game():
    """A class that holds the entire game"""
    # pythons way of stating that something is being done to a specific object is called "self"
    def __init__(self):
        pygame.init()

        self.timer = 0
        self.time_limit = 80
        self.color_index = 0
        self.color_list = self.get_color_list(4)
        self.red_box = ColorBox(RED)
        self.yellow_box = ColorBox(YELLOW)
        self.blue_box = ColorBox(BLUE)
        self.green_box = ColorBox(GREEN)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True
        self.displaying_color = True
        self.backdrop = Backdrop()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.backdrop)
        self.sprites.add(self.green_box)
        self.sprites.add(self.yellow_box)
        self.sprites.add(self.blue_box)
        self.sprites.add(self.red_box)

        # self.self_squares = SelfSquares(self.sprites, self.input)

    def get_color_list(self, squares_per_level):
        """returns random list of colors"""
        color_options = [RED, YELLOW, BLUE, GREEN]
        color_list = []
        while len(color_list) < squares_per_level:
            color = random.choice(color_options)
            color_list.append(color)
        return color_list

    def display_color_list(self):
        if self.displaying_color == True: 
            self.timer += 1
            if self.timer == self.time_limit:
                self.timer = 0
                self.clear_selection()
                color = self.color_list[self.color_index]
                self.color_index += 1

                if color == RED:
                    self.red_box.set_selected(True)
                elif color == GREEN:
                    self.green_box.set_selected(True)
                elif color == YELLOW:
                    self.yellow_box.set_selected(True)
                elif color == BLUE: 
                    self.blue_box.set_selected(True)
                # if self.color_index = len(self.color_list):
                    # self.displaying_color = False
            

            


    def clear_selection(self):
        self.red_box.set_selected(False)
        self.yellow_box.set_selected(False)
        self.blue_box.set_selected(False)
        self.green_box.set_selected(False)

            




    def update(self):
        """Updates the game"""
        self.clock.tick(FPS)
        self.display_color_list()
        # does all of the inputs and understands them
        self.handle_input()
        self.sprites.update()
        self.sprites.draw(self.screen)

        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_UP:
                    self.input["up"] = True
                elif event.key == pygame.K_DOWN:
                    self.input["down"] = True
                elif event.key == pygame.K_RIGHT:
                    self.input["right"] = True
                elif event.key == pygame.K_LEFT:
                    self.input["left"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.input["up"] = False
                elif event.key == pygame.K_DOWN:
                    self.input["down"] = False
                elif event.key == pygame.K_RIGHT:
                    self.input["right"] = False
                elif event.key == pygame.K_LEFT:
                    self.input["left"] = False

# class SelfSquares():
#     def __init__(self,sprites, input_dict):
#         self.sprites = sprites
#         self.input = input_dict

#         # Show Dull Red
        
#         self.dull_red = dull_red(self.input)
#         self.sprites.add(self.dull_red)

#         # Show Dull Green

#         self.dull_green = dull_green(self.input)
#         self.sprites.add(self.dull_green)

#         # Show Dull Blue

#         self.dull_blue = dull_blue(self.input)
#         self.sprites.add(self.dull_blue)

#         # Show Dull Yellow

#         self.dull_yellow = dull_yellow(self.input)
#         self.sprites.add(self.dull_yellow)



    
def main():
    game = Game()

    while game.running:
        game.update()

if __name__ == '__main__':
    main()