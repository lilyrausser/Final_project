import pygame

FPS = 30
WIDTH, HEIGHT = 800, 600

class Backdrop(pygame.sprite.Sprite):
    """The backdrop image for the game"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("game_background.jpg")

        self.rect = self.image.get_rect()
        self.rect.w

class bright_red(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("red_bright.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 405
        self.rect.y = 150

class dull_red(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("red_dull.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 405
        self.rect.y = 150

class bright_green(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("green_bright.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 217
        self.rect.y = 150

class dull_green(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("green_dull.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 217
        self.rect.y = 150

class bright_blue(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("blue_bright.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 217
        self.rect.y = 337

class dull_blue(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("blue_dull.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 217
        self.rect.y = 337

class bright_yellow(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("yellow_bright.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 405
        self.rect.y = 335

class dull_yellow(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()
        self.input = input_dict
        self.image = pygame.image.load("yellow_dull.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (183, 183))
        self.rect.x = 405
        self.rect.y = 335

    def update(self):
        """Updates the character sprite"""
        pass

class Game():
    """A class that holds the entire game"""
    # pythons way of stating that something is being done to a specific object is called "self"
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True

        self.input = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }

        self.backdrop = Backdrop()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.backdrop)
        self.self_squares = SelfSquares(self.sprites, self.input)

    def update(self):
        """Updates the game"""
        self.clock.tick(FPS)

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

class SelfSquares():
    def __init__(self,sprites, input_dict):
        self.sprites = sprites
        self.input = input_dict

        # Show Dull Red
        
        self.dull_red = dull_red(self.input)
        self.sprites.add(self.dull_red)

        # Show Dull Green

        self.dull_green = dull_green(self.input)
        self.sprites.add(self.dull_green)

        # Show Dull Blue

        self.dull_blue = dull_blue(self.input)
        self.sprites.add(self.dull_blue)

        # Show Dull Yellow

        self.dull_yellow = dull_yellow(self.input)
        self.sprites.add(self.dull_yellow)



    
def main():
    game = Game()

    while game.running:
        game.update()

if __name__ == '__main__':
    main()