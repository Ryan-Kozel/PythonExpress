import pygame


GRID_WIDTH = 500
GRID_HEIGHT = 500

class GameBoard:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def background_display(self):
        # fill in the game board with a checkered pattern
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x * 50, y * 50, 50, 50)
                if (x + y) % 2 == 0:
                    color = (34, 139, 34)
                else:
                    color = (144, 238, 144)

                pygame.draw.rect(self.screen, color, rect)

    def score_display(self):
        pass

    def game_over_display(self):
        pass

    def render(self, train, people):
        # 
        self.background_display()
        train.draw_train(self.screen)
        people.draw_person(self.screen)

        pygame.display.flip()