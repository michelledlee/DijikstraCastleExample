import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# This class represents the player
class Player(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Variables to hold the height and width of the block
        width = 15
        height = 15

        # Create an image of the player, and fill it with a color.
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    # Update the position of the player
    def update(self):
        # Get the current mouse position.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list
        x = pos[0]
        y = pos[1]

        # Set the attribute for the top left corner where this object is located
        self.rect.x = x
        self.rect.y = y