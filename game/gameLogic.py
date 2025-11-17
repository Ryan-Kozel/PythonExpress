import pygame, sys
from gameBoard import GameBoard
from train import Direction, Train
from people import People

GRID_WIDTH = 500
GRID_HEIGHT = 500

class GameLogic:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
        pygame.display.set_caption("PythonExpress")
        self.clock = pygame.time.Clock()

        self.score = 0
        self.board = GameBoard(self.screen, self.score)
        self.running = True
        self.game_over = False

        self.train = Train()
        self.person = People()
        self.person.randomize(list(self.train.cars))

    def run(self):
        while self.running:
            self.draw()
            self.event_handler()

        pygame.quit()
        sys.exit()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                else:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.train.turn(Direction.UP)
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.train.turn(Direction.DOWN)
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.train.turn(Direction.LEFT)
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.train.turn(Direction.RIGHT)

    def update(self):
        if self.game_over:
            self.board.game_over_display()
            return
        
        self.train.move_train()
        front_car = self.train.cars[0]

        if self.check_people_collision():
            self.train.car_awaiting += 1
            self.score += 10

    def draw(self):
        self.board.render(self.train, self.person)

