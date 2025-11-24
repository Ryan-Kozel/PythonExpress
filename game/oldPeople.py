import pygame
import random
from people import People

GRID_WIDTH = 500
GRID_HEIGHT = 500
SQUARE_SIZE = 50

class OldPeople(People):
    def __init__(self):
        super().__init__()
        self.randomize()
        self.old_person_sprite = pygame.image.load('graphics/old_person.png')
        self.old_person_sprite = pygame.transform.scale(self.old_person_sprite, (SQUARE_SIZE, SQUARE_SIZE))

    def randomize(self, occupied_pos=None):
        # check if there are any occupied positions by the train
        if occupied_pos is None:
            occupied_pos = []

        # spawn people randomly around the grid
        while True:
            corners = [
                (0, 0),
                (0, (GRID_HEIGHT // SQUARE_SIZE) - 1),
                ((GRID_WIDTH // SQUARE_SIZE) - 1, 0),
                ((GRID_WIDTH // SQUARE_SIZE) - 1, (GRID_HEIGHT // SQUARE_SIZE) - 1)
            ]
            avail = [c for c in corners if c not in occupied_pos]
            # if the generated position is not taken by the train set the new position
            if avail:
                self.position = random.choice(corners)
                break

    def draw_person(self, surface):
        x, y = self.position
        people_rect = pygame.Rect(x * SQUARE_SIZE,y * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
        surface.blit(self.old_person_sprite, people_rect.topleft)

