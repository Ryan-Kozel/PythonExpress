import pygame
import random

GRID_WIDTH = 700
GRID_HEIGHT = 700

class People:
    def __init__(self):
        self.position = (0,0)
        self.randomize()

    def randomize(self, occupied_pos=None):
        # check if there are any occupied positions by the train
        if occupied_pos is None:
            occipied_pos = []

        # spawn people randomly around the grid
        while True:
            x = random.randint(0, GRID_WIDTH-1)
            y = random.randint(0, GRID_HEIGHT-1)
            rand_pos = (x,y)

            if rand_pos not in occupied_pos:
                self.positon = rand_pos
                break
    
    # NEEDS IMPLEMENTATION
    def draw(self, surface): 
        pass