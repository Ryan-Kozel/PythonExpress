import pygame
import random

GRID_WIDTH = 500
GRID_HEIGHT = 500
SQUARE_SIZE = 50

class People:
    def __init__(self):
        # spawn the first person at a random location on the board
        self.position = (0,0)
        self.randomize()
        self.person_sprite = pygame.image.load('graphics/person.png')
        self.person_sprite = pygame.transform.scale(self.person_sprite, (SQUARE_SIZE,SQUARE_SIZE))

    def randomize(self, occupied_pos=None):
        # check if there are any occupied positions by the train
        if occupied_pos is None:
            occupied_pos = []

        # spawn people randomly around the grid
        while True:
            x = random.randint(0, (GRID_WIDTH // SQUARE_SIZE)-1)
            y = random.randint(0, (GRID_HEIGHT // SQUARE_SIZE)-1)
            rand_pos = (x,y)
            # if the generated position is not taken by the train set the new position
            if rand_pos not in occupied_pos:
                self.position = rand_pos
                break
    
    def draw_person(self, surface):
        x, y = self.position
        people_rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        surface.blit(self.person_sprite, people_rect.topleft)