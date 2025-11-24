import pygame
from enum import Enum
from collections import deque

SQUARE_SIZE = 50

class Direction(Enum):
    UP = (0,-1)
    DOWN = (0,1)
    LEFT = (-1,0)
    RIGHT = (1,0)

class Train:
    def __init__(self):
        self.start_pos = (4, 4)
        self.start_len = 3
        self.cars = deque()
        self.car_awaiting = 0
        self.direction = Direction.UP
        self.next_dir = Direction.UP

        self.train_up_sprite = pygame.image.load('graphics/train_up.png')
        self.train_up_sprite = pygame.transform.scale(self.train_up_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        self.train_down_sprite = pygame.image.load('graphics/train_down.png')
        self.train_down_sprite = pygame.transform.scale(self.train_down_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        self.train_left_sprite = pygame.image.load('graphics/train_left.png')
        self.train_left_sprite = pygame.transform.scale(self.train_left_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        self.train_right_sprite = pygame.image.load('graphics/train_right.png')
        self.train_right_sprite = pygame.transform.scale(self.train_right_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        self.car_up_sprite = pygame.image.load('graphics/car_up.png')
        self.car_up_sprite = pygame.transform.scale(self.car_up_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        self.car_down_sprite = pygame.image.load('graphics/car_down.png')
        self.car_down_sprite = pygame.transform.scale(self.car_down_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        self.car_left_sprite = pygame.image.load('graphics/car_left.png')
        self.car_left_sprite = pygame.transform.scale(self.car_left_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        self.car_right_sprite = pygame.image.load('graphics/car_right.png')
        self.car_right_sprite = pygame.transform.scale(self.car_right_sprite, (SQUARE_SIZE,SQUARE_SIZE))

        # create the train on initialization
        x,y = self.start_pos
        for car in range(self.start_len):
            self.cars.append((x, y+car))

    def draw_train(self, surface):
        # create each car with a pygame rect
        for i, (x,y) in enumerate(self.cars):
            car_rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            
            # the head car will be a different color
            if i == 0:
                if self.direction == Direction.UP:
                    surface.blit(self.train_up_sprite, car_rect.topleft)
                elif self.direction == Direction.DOWN:
                    surface.blit(self.train_down_sprite, car_rect.topleft)
                elif self.direction == Direction.LEFT:
                    surface.blit(self.train_left_sprite, car_rect.topleft)
                elif self.direction == Direction.RIGHT:
                    surface.blit(self.train_right_sprite, car_rect.topleft)
            else:
                if self.direction == Direction.UP:
                    surface.blit(self.car_up_sprite, car_rect.topleft)
                elif self.direction == Direction.DOWN:
                    surface.blit(self.car_down_sprite, car_rect.topleft)
                elif self.direction == Direction.LEFT:
                    surface.blit(self.car_left_sprite, car_rect.topleft)
                elif self.direction == Direction.RIGHT:
                    surface.blit(self.car_right_sprite, car_rect.topleft)     

    def move_train(self):
        self.direction = self.next_dir
        # create the new head
        x,y = self.cars[0]
        dx, dy = self.direction.value
        new_car = (x + dx, y + dy)
        self.cars.appendleft(new_car)

        # if no cars are being added, remove the last car
        if self.car_awaiting == 0:
            self.cars.pop()
        # otherwise keep train plus new car to extend length
        else:
            self.car_awaiting -= 1

        return new_car
    
    def turn(self, new_dir):
        # 180 degree turns are an invalid operation
        invalid_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        # check if the turn being made is invalid
        if new_dir != invalid_directions.get(self.direction):
            self.next_dir = new_dir

    def check_collision(self):
        # head cannot collide with the rest of the train
        # check if the head pos is in the list of cars excluding the front
        head = self.cars[0]
        return head in list(self.cars)[1:]