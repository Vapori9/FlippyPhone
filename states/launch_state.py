from states.state import *
class Launch_state(State):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        State.__init__(self, sys_settings)

        # standard phone state shit
        self.standard_phone_background = pygame.image.load("assets/standardMainSelection.png").convert_alpha()
        self.standard_phone_background = pygame.transform.scale(self.standard_phone_background, size)
        self.flippyphone_icon_rect = (RS*360, RS*600, RS*100, RS*110)


    def update(self, click):
        # checks if there has been a click this current frame
        if (click != None):
            # assing hitbox with mouse position and width and height of 2
            clickRect = (click[0], click[1], 2, 2)

            # Check if collides with a event hitbox that requests the next state to be changed
            if (rectCollision(self.flippyphone_icon_rect, clickRect)):
                self.exit_state = 1

    def render(self, display):
        display.blit(self.standard_phone_background, (0, 0))


