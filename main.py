import pygame
from settings import *

# Moi murut, jos valittaa että pygame ei asennettu tms ja käytette pycharmia niin
# 1-> File yläkulmasta
# 2-> Settings
# 3-> Project interpreter
# 4-> "+" merkki (Install ku hoveraa sen päällä)
# 5-> Hakekaa pygame ja install package



pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FlippyPhone")

# Initialization of pygame must be done prior
from application import Application


# -------- Main Program Loop -----------
def main():
    done = False
    clock = pygame.time.Clock()

    application = Application()

    while not done:
        current_click = None
        # checks for events, here only checking mouse clicks if necessary, since we are doing a
        # "touch screen" device
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # exits the loop
                done = True

            # if user presses some mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if the button is the left button
                if (pygame.mouse.get_pressed()[0] == True):

                    # set the click coordinates to this variable, by default this is null
                    current_click = pygame.mouse.get_pos()

        # Fills the screen with black color
        screen.fill((0, 0, 0))

        # The application is updated
        application.update(current_click)

        # The contents of the window are drawn
        application.render(screen)

        # The window is updated (shows the drawn contents)
        pygame.display.flip()

        # Caps the application to run at max 60 fps
        clock.tick(60)
    # If the user shuts down the window, exit the program.
    pygame.quit()









main()