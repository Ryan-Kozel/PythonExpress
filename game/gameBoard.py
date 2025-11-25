import easygui
import pygame
from easygui import enterbox
from playerProfiles import PlayerProfiles

# User input for player name. Draw before anything else to prevent errors with MacOS
player_name= easygui.enterbox(msg="Enter Username:")

if not player_name:
    player_name= 'Player'


GRID_WIDTH = 500
GRID_HEIGHT = 500
SQUARE_SIZE = 50

class GameBoard:
    def __init__(self, screen, score, high_score):
        self.screen = screen
        self.score = score
        self.high_score = high_score
        self.font = pygame.font.Font(None, 36)
        self.profiles = PlayerProfiles()
        self.state ='start'
        self.scoresaved = False

    def display_start_screen(self):
        """Display a simple start screen so the player can choose when game starts"""
        start_screen = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        self.screen.blit(start_screen, (0, 0))

        welcome_text = self.font.render("Welcome to PythonExpress", True, (255, 255, 255))
        enter_text = self.font.render("Press Space or Enter to Start", True, (255, 255, 255))

        # Offset the enter_text so it does not overlap
        # Offset by the height of the welcome_text + height of enter_text
        self.screen.blit(welcome_text, (10, 10))
        self.screen.blit(enter_text, (10, welcome_text.get_height() + enter_text.get_height()))
        pygame.display.flip()

    def background_display(self):
        """Fill the board with a checkered pattern of equal size squares"""
        for y in range(GRID_HEIGHT // SQUARE_SIZE):
            for x in range(GRID_WIDTH // SQUARE_SIZE):
                rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                # Color every other square a different color
                if (x + y) % 2 == 0:
                    color = (34, 139, 34)
                else:
                    color = (144, 238, 144)

                pygame.draw.rect(self.screen, color, rect)

    def score_display(self):
        """Overlay the player score in the top left corner"""
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10,10))

    def game_over_display(self):
        """Generate a display for when the game is over and save the player's score to CSV"""
        # Save players score to CSV file when game is over
        if not self.scoresaved:
            self.profiles.save_score(player_name, self.score, self.high_score)
            self.scoresaved = True

        #Create overlay that is semi transparent for the end game screen with
        #End game text including score
        end_overlay = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
        end_overlay.set_alpha(175)
        self.screen.blit(end_overlay, (0, 0))

        # Text for game over screen
        game_over_text = self.font.render("GAME OVER", True, (255, 255, 255))
        score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, (255, 255, 255))

        # Format the text to not overlap
        self.screen.blit(game_over_text, (10, 10))
        self.screen.blit(score_text, (10, game_over_text.get_height() + score_text.get_height()))
        self.screen.blit(high_score_text, (10, score_text.get_height() + high_score_text.get_height() + 20))
        pygame.display.flip()

    def render(self, train, people, old, game_over=False):
        """Render the correct screen depending on game state"""
        # Only draw start screen when app first opened
        if self.state == 'start':
            print('Drawing start screen')
            self.display_start_screen()

        # Only draw game over screen when the game is done
        elif game_over:
            print("Game over")
            self.game_over_display()

        # Draw background layers first and the top layers last
        else:
            print("Generating game")
            self.background_display()
            train.draw_train(self.screen)
            people.draw_person(self.screen)
            old.draw_person(self.screen)
            self.score_display()
        pygame.display.flip()