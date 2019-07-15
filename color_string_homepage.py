import pygame 
FPS = 30 
WIDTH, HEIGHT = 800, 600

class Backdrop(pygame.sprite.Sprite): 
    """The background image for the game"""
    def __init__(self): 
        super().__init__()
        
        self.image = pygame.image.load("homepage.JPG")

        self.rect = self.image.get_rect()



class Character(pygame.sprite.Sprite): 
    """The quit character"""
    def __init__(self): 
        super().__init__()

        self.image = pygame.image.load("play_button2.png")

        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (140,100))

        self.rect.x = HEIGHT / 2 

        self.rect.y = 400


# score 
class Game(): 
    """A class that holds the entire game"""
    def __init__(self): 
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True

        self.backdrop = Backdrop()
        self.character = Character()

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.backdrop)
        self.sprites.add(self.character)


    
    def update(self): 
        self.clock.tick(FPS)

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
                elif event.key == pygame.K_w:
                    self.input["up"] = True
                elif event.key == pygame.K_s:
                    self.input["down"] = True
                elif event.key == pygame.K_a:
                    self.input["left"] = True
                elif event.key == pygame.K_d:
                    self.input["right"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.input["up"] = False
                elif event.key == pygame.K_s:
                    self.input["down"] = False
                elif event.key == pygame.K_a:
                    self.input["left"] = False
                elif event.key == pygame.K_d:
                    self.input["right"] = False







def main(): 
    game = Game()

    while game.running: 
        game.update()


if __name__ == '__main__': 
    main()













