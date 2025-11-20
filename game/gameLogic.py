import pygame, sys
from gameBoard import GameBoard
from train import Direction, Train
from people import People

GRID_WIDTH = 500
GRID_HEIGHT = 500

class GameLogic:
    def __init__(self):
        pygame.init()
        # create game window
        self.screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
        # set window title to game name
        pygame.display.set_caption("PythonExpress")
        # initialize variable to control how fast the game is running
        self.clock = pygame.time.Clock()

        self.score = 0
        self.board = GameBoard(self.screen, self.score)
        self.running = True

        # initialize game score, train, and spawn first person object
        self.game_over = False

        self.train = Train()
        self.person = People()
        self.person.randomize(list(self.train.cars))

    def run(self):
        while self.running:
            self.draw()
            self.event_handler()
            self.update()
            # FPS controller
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

    def event_handler(self):
        for event in pygame.event.get():
            # stop the game if exited
            if event.type == pygame.QUIT:
                self.running = False

            # handle key events
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    # reset the game with space bar
                    if event.key == pygame.K_SPACE:
                        self.reset()
                else:
                    # move the train up
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.train.turn(Direction.UP)
                    # move the train down
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.train.turn(Direction.DOWN)
                    # move the train left
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.train.turn(Direction.LEFT)
                    # move the train right
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.train.turn(Direction.RIGHT)

    def update(self):
        if self.game_over:
            print('game over')
            self.board.game_over_display()
            return
        
        # keep the train moving once the game starts
        self.train.move_train()
        front_car = self.train.cars[0]

        # check for a collision with a person object
        if self.person_collision():
            # add a car and increase the score, then generate a new person
            self.train.car_awaiting += 1
            self.score += 10
            self.person.randomize(list(self.train.cars))

        if self.train.check_collision():
            # end the game 
            self.game_over = True
            return
        
        if self.wall_collision(front_car):
            # end the game
            self.game_over = True
            return
        # when the "next level" is reached, increase boardsize but preserve train length
        if self.next_level(self.score):
            # take current length
            cur_length = len(self.train.cars)
            self.game_over = False

            # recreate train with previous length
            self.train = Train()
            self.train.start_len = cur_length
            self.train.create_new_train(self.train.start_pos)

            # spawn people the same
            self.person = People()
            self.person.randomize(list(self.train.cars))

            # increase board size
        self.board.score = self.score

    def draw(self):
        # draw the train and person objects
        self.board.render(self.train, self.person)

    def person_collision(self):
        # check if the front of the train collides with person obejct
        return self.train.cars[0] == self.person.position

    def wall_collision(self, position):
        # check if the front of the train collides with wall
        x, y = position
        return x < 0 or x >= GRID_WIDTH // 50 or y < 0 or y >= GRID_HEIGHT // 50
    
    def next_level(self, score):
        # if the play reaches 1 of the three scores, extend the board
        return score == 100 or score == 200 or score == 300
    
    def reset(self):
        self.game_over = False
        self.score = 0
        self.train = Train()
        self.person = People()
        self.person.randomize(list(self.train.cars))

