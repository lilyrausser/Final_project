import pygame

# if you don't plan on changing the variable (constant), then best practice to make it capitalied
FPS = 30
WIDTH, HEIGHT = 800, 600

class Backdrop(pygame.sprite.Sprite):
    """The backdrop image for the game"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/rules.jpg")

        self.rect = self.image.get_rect()
        self.rect.w

class Character(pygame.sprite.Sprite):
    """The game's character"""
    def __init__(self, input_dict):
        super().__init__()

        self.input = input_dict

        self.x, self.y = 0,0
        self.vx, self.vy = 0,0
        self.ax, self.ay = 0,0

        self.images = {}
        self.image = pygame.image.load("assets/back_button.png")
        
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (70, 50))

        self.rect.x = 670
    
        self.rect.y = 20


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
        self.character = Character(self.input)

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.backdrop)
        self.sprites.add(self.character)

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

def main():
    game = Game()

    while game.running:
        game.update()

if __name__ == '__main__':
    main()