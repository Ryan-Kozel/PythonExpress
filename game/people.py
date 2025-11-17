import pygame
import random

GRID_WIDTH = 500
GRID_HEIGHT = 500

class People:
    def __init__(self):
        self.position = (0,0)
        self.randomize()

    def randomize(self, occupied_pos=None):
        # check if there are any occupied positions by the train
        if occupied_pos is None:
            occupied_pos = []

        # spawn people randomly around the grid
        while True:
            x = random.randint(0, GRID_WIDTH-1)
            y = random.randint(0, GRID_HEIGHT-1)
            rand_pos = (x,y)

            if rand_pos not in occupied_pos:
                self.position = rand_pos
                break
    
    # NEEDS IMPLEMENTATION
    def draw_person(self, surface): 
        x, y = self.position
        people_rect = pygame.Rect(x * 50,y * 50,50,50)
        pygame.draw.rect(surface, (220,20,60), people_rect)
        pygame.draw.rect(surface, (0,0,0), people_rect, 2)