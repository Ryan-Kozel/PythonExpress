import pygame


GRID_WIDTH = 500
GRID_HEIGHT = 500

class GameBoard:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font(None, 36)
        #Change to 'start' to see start screen
        self.state ='s'

    #TODO
    def display_start_screen(self):

        start_screen = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        self.screen.blit(start_screen, (0, 0))

        welcome_text = self.font.render("Welcome to PythonExpress", True, (255, 255, 255))
        enter_text = self.font.render("Please Enter Username:", True, (255, 255, 255))

        self.screen.blit(welcome_text, (10, 10))
        self.screen.blit(enter_text, (10, welcome_text.get_height() + enter_text.get_height()))

        pygame.display.flip()

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
        #Create score text
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10,10))


    def game_over_display(self):
        #Create overlay that is semi transparent for the end game screen with
        #End game text including score
        end_overlay = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        end_overlay.set_alpha(175)
        self.screen.blit(end_overlay, (0, 0))

        game_over_text = self.font.render("GAME OVER", True, (255, 255, 255))
        score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))


        self.screen.blit(game_over_text, (10, 10))
        self.screen.blit(score_text, (10, game_over_text.get_height() + score_text.get_height()))
        pygame.display.flip()

    def render(self, train, people):
        #
        if self.state == 'start':
            self.display_start_screen()
        else:
            self.background_display()
            train.draw_train(self.screen)
            people.draw_person(self.screen)
            # Generate the top layers last, for example if score_display() goes first, the background will cover it up
            self.score_display()
        pygame.display.flip()