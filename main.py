import pygame, sys, time
from settings import *
 
 
class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Breakout')
 
    def run(self):
        last_time = time.time()
        while True:
            
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
 
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            # update window
            pygame.display.update()
 
if __name__ == '__main__':
    game = Game()
    game.run()
 