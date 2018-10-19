import pygame
import Player
import Ghost

STEP_SIZE = 15
WINDOW_WIDTH = 54 * STEP_SIZE
WINDOW_HEIGHT = 40 * STEP_SIZE

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GHOST_COLOURS = ["ghost1.png", "ghost2.png", "ghost3.png"]
GREEN_GHOST = ["ghost2.png"]
PURPLE_GHOST = ["ghost3.png"]

pygame.init()

# Set the height and width of the screen
size = [WINDOW_WIDTH, WINDOW_HEIGHT]
screen = pygame.display.set_mode(size)

# Don't display the mouse pointer
pygame.mouse.set_visible(False)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Sprite list
all_sprites_list = pygame.sprite.Group()

# Game characters
player = Player.Player()
annoying = Ghost.AnnoyingGhost()    # Creates an AnnoyingGhost
annoying.setX(100)
annoying.setY(100)
shy = Ghost.ShyGhost()              # Creates a ShyGhost
shy.setX(500)
shy.setY(100)
shy.setColours(GREEN_GHOST)
cultured = Ghost.CulturedGhost()    # Creates a Culturedghost
cultured.setX(100)
cultured.setY(500)
cultured.setColours(PURPLE_GHOST)
robo = Ghost.RobotGhost()           # Creates a RobotGhost
robo.setX(500)
robo.setY(500)

# Add the ball to the list of player-controlled objects
all_sprites_list.add(player)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing to screen
    all_sprites_list.update()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    # Game logic
    print("ANNOYING GHOST:")
    annoying.go_home(player.rect.x, player.rect.y)
    annoying.be_flashy(GHOST_COLOURS)
    annoying.draw(screen, annoying._ghost_surf)
    annoying.boo()
    annoying.move()
    # annoying.lights_on() # Cannot be called since annoying ghost does not have the lightsOn method

    print("SHY GHOST:")
    shy.draw(screen, shy._ghost_surf)
    shy.boo()
    shy.lights_on()
    shy.run(player.rect.x, player.rect.y)
    shy.move()

    print("CULTURED GHOST:")
    cultured.draw(screen, cultured._ghost_surf)
    cultured.boo()
    cultured.go_home()
    # cultured.lights_on() # Cannot be called since cultured ghost does not have the lightsOn method

    print("ROBO GHOST:")
    robo.draw(screen, robo._ghost_surf)
    robo.boo()
    robo.lights_on()
    robo.run()
    robo.be_flashy(GHOST_COLOURS)
    robo.move()

    clock.tick(35)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()