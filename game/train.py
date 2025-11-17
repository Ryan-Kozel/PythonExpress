import pygame
from enum import Enum
from collections import deque

class Direction(Enum):
    UP = (0,-1)
    DOWN = (0,1)
    LEFT = (-1,0)
    RIGHT = (1,0)

class Train:
    def __init__(self):
        self.start_pos = (0, 0)
        self.start_len = 3
        self.cars = deque()
        self.car_awaiting = 0
        self.direction = Direction.UP
        self.next_dir = Direction.UP

        # create the train on initialization
        x,y = self.start_pos
        for car in range(self.start_len):
            self.cars.append((x-car, y))

    # NEEDS IMPLEMENTATION
    def draw_train(self, surface):
        for i, (x,y) in enumerate(self.cars):
            car_rect = pygame.Rect(int(x * 50),int(y * 50),50,50)
            
            if i == 0:
                pygame.draw.rect(surface, (220, 20, 60), car_rect)
            else:
                pygame.draw.rect(surface, (139, 0, 0), car_rect)
            pygame.draw.rect(surface, (0,0,0), car_rect, 1)
        

    def move_train(self):
        self.direction = self.next_dir
        # create the new head
        x,y = self.cars[0]
        new_car = (x + self.direction.value, y + self.direction.value)
        self.cars.appendleft(new_car)

        # if no cars are being added, remove the last car
        if self.car_awaiting == 0:
            self.cars.pop()
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