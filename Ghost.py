import pygame
import math
from random import randint

from Strategy import LoudBooStrategy
from Strategy import GentleBooStrategy
from Strategy import BrightLightsStrategy

# Store strategy functions
loud_boo = LoudBooStrategy()
gentle_boo = GentleBooStrategy()
ten_seconds = BrightLightsStrategy()

# Global Variables
STEP_SIZE = 15
WINDOW_WIDTH = 54 * STEP_SIZE
WINDOW_HEIGHT = 40 * STEP_SIZE
MAX_VELOCITY = 5
MIN_DISTANCE = 15
GHOST_COLOURS = ["ghost1.png", "ghost2.png", "ghost3.png"]

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Ghost(object):
    x = 0
    y = 0
    velocityx = 0
    velocityy = 0
    direction = 0
    orientation = 0
    colours = ["ghost1.png"]

    def __init__(self, boo_strategy, light_strategy):
        self._ghost_surf = pygame.image.load(self.colours[0]).convert()
        self.velocityx = randint(1, 10) / 10.0
        self.velocityy = randint(1, 10) / 10.0

        self._boo_strategy = boo_strategy
        self._light_strategy = light_strategy

    # Define strategy functions for the Ghost class
    def boo(self):
        self._boo_strategy.boo()

    # Define strategy functions for the Ghost class
    def lights_on(self):
        self._light_strategy.lights_on()

    # Set starting coordinates for x
    def setX(self, x):
        self.x = x

    # Set starting coordinates for y
    def setY(self, y):
        self.y = y

    # Set colour
    def setColours(self, colours):
        self.colours = colours

    # Function draws the object to screen
    def draw(self, surface, image):
        length = len(self.colours)
        if length == 1:
            self._ghost_surf = pygame.image.load(self.colours[0]).convert()
        else:
            self._ghost_surf = pygame.image.load(self.colours[randint(0, length-1)]).convert()
        surface.blit(image, (self.x, self.y))

    # Function calculates the distance between the ghost and another object
    def distance(self, ghost):
        distx = self.x - ghost.x
        disty = self.y - ghost.y
        return math.sqrt(distx * distx + disty * disty)

    # Function controls the movement of the bird object
    def move(self):
        if abs(self.velocityx) > MAX_VELOCITY or abs(self.velocityy) > MAX_VELOCITY:
            scaleFactor = MAX_VELOCITY / max(abs(self.velocityx), abs(self.velocityy))
            self.velocityx *= scaleFactor
            self.velocityy *= scaleFactor

        self.x += self.velocityx
        self.y += self.velocityy

    # Function determines whether two objects have collided by comparing where the origin corners of
    # the shape are and the total size of each object
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 < x2 + bsize and x1 + bsize > x2 and y1 < y2 + bsize and y1 + bsize > y2:
            return True
        return False

    # Function makes the ghost chase the player
    def target(self, dx, dy):

        distancex = 0
        distancey = 0

        # If the chaser and chasee aren't touching, continue chasing by reducing the
        # distance between the two
        if dx != self.x and dy != self.y:
            distancex += (self.x - dx)
            distancey += (self.y - dy)

        # If they have collided, the chaser is on top of the target
        if self.isCollision(self.x, self.y, dx, dy, MIN_DISTANCE):
            self.x = dx
            self.y = dy

        # Speed for the chase
        self.velocityx -= distancex
        self.velocityy -= distancey

    # Function makes the ghost run away from the player
    def evade(self, dx, dy):

        distancex = 0
        distancey = 0

        # If the chaser and chasee aren't touching, continue running by increasing the
        # distance between the two
        if dx != self.x and dy != self.y:
            distancex += (self.x + dx) * .001
            distancey += (self.y + dy) * .001

        # If the mouse is to the bottom or right of the ghost
        if dx > self.x and dy > self.y:
            self.velocityx -= distancex
            self.velocityy -= distancey

        # If the mouse is to the top or left of the ghost
        if dx < self.x and dy < self.y:
            self.velocityx += distancex
            self.velocityy += distancey

    # Function makes the ghost seek the player
    def seek(self, dx, dy):

        distancex = 0
        distancey = 0

        # If the chaser and chasee aren't touching, continue chasing by reducing the
        # distance between the two
        if dx != self.x and dy != self.y:
            distancex += (self.x - dx)
            distancey += (self.y - dy)

        # Speed for the chase
        self.velocityx -= distancex
        self.velocityy -= distancey

    # Function makes the ghost NPC wander around
    def wander(self):

        # Randomly select the next direction to go to
        nextdirection = randint(0, 7)

        # Number of steps to go in that direction
        numberofsteps = randint(0, 3)

        # Cases for each direction
        if nextdirection == 0:
            dx = self.x
            dy = MIN_DISTANCE - self.y

            # Seek to the new direction
            self.seek(dx, dy)

        # Move to the direction wandered to
        if nextdirection == 0:      # North
            dx = self.x
            dy = self.y - (MIN_DISTANCE * numberofsteps)

            # Seek to the new direction
            self.seek(dx, dy)
        elif nextdirection == 1:    # North East
            dx = self.x + (MIN_DISTANCE * numberofsteps)
            dy = self.y - (MIN_DISTANCE * numberofsteps)

            # Seek to the new direction
            self.seek(dx, dy)
        elif nextdirection == 2:    # East
            dx = self.x + (MIN_DISTANCE * numberofsteps)
            dy = self.y

            # Seek to the new direction
            self.seek(dx, dy)
        elif nextdirection == 3:    # South East
            dx = self.x + (MIN_DISTANCE * numberofsteps)
            dy = self.y + (MIN_DISTANCE * numberofsteps)

            # Seek to the new direction
            self.seek(dx, dy)
        elif nextdirection == 4:    # South
            dx = self.x
            dy = self.y + (MIN_DISTANCE * numberofsteps)

            # Seek to the new direction
            self.seek(dx, dy)
        elif nextdirection == 5:    # South West
            dx = self.x - (MIN_DISTANCE * numberofsteps)
            dy = self.y + (MIN_DISTANCE * numberofsteps)

            # Seek to the new direction
            self.seek(dx, dy)
        elif nextdirection == 6:    # West
            dx = self.x - (MIN_DISTANCE * numberofsteps)
            dy = self.y

            # Seek to the new direction
            self.seek(dx, dy)
        else:    # North West
            dx = self.x - (MIN_DISTANCE * numberofsteps)
            dy = self.y - (MIN_DISTANCE * numberofsteps)

            # Seek to the new direction
            self.seek(dx, dy)

# AnnoyingGhost which has a boo strategy but no light strategy
class AnnoyingGhost(Ghost):
    def __init__(self):
        super(AnnoyingGhost, self).__init__(loud_boo, None)
        self.colours = GHOST_COLOURS

    def go_home(self, dx, dy):
        print("Wait for me!")
        self.seek(dx, dy)

    def be_flashy(self, colours):
        self.colours = colours

# ShyGhost which has a boo strategy and a light strategy
class ShyGhost(Ghost):
    def __init__(self):
        super(ShyGhost, self).__init__(gentle_boo, ten_seconds)

    def run(self, dx, dy):
        print("Leave me alone!")
        self.evade(dx, dy)

# CulturedGhost which has a boo strategy but no light strategy
class CulturedGhost(Ghost):
    def __init__(self):
        super(CulturedGhost, self).__init__(gentle_boo, None)

    def go_home(self):
        print("I need a rest back at the art gallery.")

# RobotGhost which has a boo strategy and a light strategy
class RobotGhost(Ghost):
    def __init__(self):
        super(RobotGhost, self).__init__(loud_boo, ten_seconds)

    def run(self):
        print("Searching!")
        self.wander()

    def be_flashy(self, colours):
        self.colours = colours
