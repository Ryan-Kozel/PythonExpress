import pygame, sys
from gameBoard import GameBoard, player_name
from train import Direction, Train
from people import People
from oldPeople import OldPeople

GRID_WIDTH = 500
GRID_HEIGHT = 500
SQUARE_SIZE = 50

class GameLogic:
    def __init__(self):
        pygame.init()
        # create game window
        self.screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
        # set window title to game name
        pygame.display.set_caption("PythonExpress")
        # initialize variable to control how fast the game is running
        self.clock = pygame.time.Clock()
        self.fps = 5

        self.score = 0
        self.high_score = 0
        self.board = GameBoard(self.screen, self.score, self.high_score)
        # display the start screen until player input is given
        self.wait()
        self.running = True

        # initialize game score, train, and spawn first person object
        self.game_over = False

        self.train = Train()
        self.person = People()
        self.old_person = OldPeople()
        self.person.randomize(list(self.train.cars) + [self.old_person.position])
        self.old_person.randomize(list(self.train.cars) + [self.person.position])

    def wait(self):
        # keep the start screen display on until the player inputs space or enter
        idle = True
        while idle: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        idle = False
                        self.board.state = 'Running'

            self.board.display_start_screen()
            self.clock.tick(10)

        self.high_score = self.board.profiles.get_high_score(player_name)
        self.board.high_score = self.high_score

    def run(self):
        while self.running:
            self.draw()
            self.event_handler()
            self.update()
            # FPS controller
            self.clock.tick(self.fps)

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
            return
        
        # keep the train moving once the game starts
        self.train.move_train()
        front_car = self.train.cars[0]

        # check for a collision with a person object
        if self.person_collision(front_car):
            # add a car and increase the score, then generate a new person
            self.train.car_awaiting += 1
            self.score += 10
            self.person.randomize(list(self.train.cars) + [self.old_person.position])

        if self.old_person_collision(front_car):
            self.train.car_awaiting += 1
            self.score += 20
            self.old_person.randomize(list(self.train.cars) + [self.person.position])

        if self.train.check_collision():
            # end the game 
            self.game_over = True
            return
        
        if self.wall_collision(front_car):
            # end the game
            self.game_over = True
            return
        
        # when the "next level" is reached, increase game speed
        if self.next_level(self.score):
            # increase game speed by 5 frames per level
            if self.score == 100:
                self.fps = 7

            if self.score == 200:
                self.fps = 10

            if self.score == 300:
                self.fps = 13

        # update score and high score during the game
        self.board.score = self.score
        if (self.high_score < self.score):
            self.high_score = self.score
            self.board.high_score = self.score

    def draw(self):
        # draw the train and person objects
        self.board.render(self.train, self.person, self.old_person, self.game_over)

    def person_collision(self, front_car):
        # check if the front of the train collides with person object
        return front_car == self.person.position
    
    def old_person_collision(self, front_car):
        # check if the front of the train collides with old_person object
        return front_car == self.old_person.position

    def wall_collision(self, front_car):
        # check if the front of the train collides with wall
        x, y = front_car
        return x < 0 or x >= GRID_WIDTH // SQUARE_SIZE or y < 0 or y >= GRID_HEIGHT // SQUARE_SIZE
    
    def next_level(self, score):
        # if the play reaches 1 of the three scores, extend the board
        return score == 100 or score == 200 or score == 300
    
    def reset(self):
        self.game_over = False
        self.board.scoresaved = False
        self.fps = 5
        self.score = 0
        self.train = Train()
        self.person = People()
        self.old_person = OldPeople()
        self.person.randomize(list(self.train.cars) + [self.old_person.position])
        self.old_person.randomize(list(self.train.cars) + [self.person.position])

