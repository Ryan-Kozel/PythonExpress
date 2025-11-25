import pygame
import random
from people import People

GRID_WIDTH = 500
GRID_HEIGHT = 500
SQUARE_SIZE = 50

class OldPeople(People):
    def __init__(self):
        # Treat as normal person
        super().__init__()
        self.randomize()
        self.old_person_sprite = pygame.image.load('graphics/old_person.png')
        self.old_person_sprite = pygame.transform.scale(self.old_person_sprite, (SQUARE_SIZE, SQUARE_SIZE))

    def randomize(self, occupied_pos=None):
        """Randomly spawn an old person worth 20 points. They can only spawn in the corners of the board"""
        # Check if there are any occupied positions by the train
        if occupied_pos is None:
            occupied_pos = []

        last_pos = self.position
        # Spawn people randomly around the grid
        while True:
            # All 4 possible spawn locations
            corners = [
                (0, 0),
                (0, (GRID_HEIGHT // SQUARE_SIZE) - 1),
                ((GRID_WIDTH // SQUARE_SIZE) - 1, 0),
                ((GRID_WIDTH // SQUARE_SIZE) - 1, (GRID_HEIGHT // SQUARE_SIZE) - 1)
            ]

            #Create a list of possible corners to spawn that are not taken up by the train
            avail = [c for c in corners if c not in occupied_pos]

            # Only spawn if there are available spaces
            if avail:
                # Try to remove the most recent position from the list of available spaces
                # This does not allow old people to keep spawning in the same corner
                try:
                    avail.remove(last_pos)
                except ValueError as e:
                    print("Old person last_pos not in a corner")
                finally:
                    # Update current position
                    self.position = random.choice(avail)
                    break

    def draw_person(self, surface):
        """Draw the old person with their sprite"""
        x, y = self.position
        people_rect = pygame.Rect(x * SQUARE_SIZE,y * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
        surface.blit(self.old_person_sprite, people_rect.topleft)

