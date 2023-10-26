from states.state import *

class FlippyPhone_main_state(State):
    def __init__(self, sys_settings):
        State.__init__(self, sys_settings)


        # Flippyphone opened
        self.flippyPhone_opened_image = pygame.image.load("assets/flippyOpened.png")
        self.flippyPhone_opened_image = pygame.transform.scale(self.flippyPhone_opened_image,
                                                               ((int(size[0] / 2)), size[1]))

        self.close_phone_button_rect = (0, size[1]*0.06, size[0], size[1]*0.94)

        self.widen_phone_button_rect = (0, 0, size[0], size[1]*0.05)

        self.close_sound = pygame.mixer.Sound("sounds/close_flap.wav")

    def update(self, click):
        if (click != None):
            clickRect = (click[0], click[1], 2, 2)
            if (rectCollision(self.close_phone_button_rect, clickRect)):
                self.exit_state = 3
                self.close_sound.play()

            if (rectCollision(self.widen_phone_button_rect, clickRect)):
                self.exit_state = 5

    def render(self, display):
        display.blit(self.flippyPhone_opened_image, (size[0] / 2 - size[0] / 4, 0))
        #pygame.draw.rect(display, (0, 150, 200), self.close_phone_button_rect) # No need to draw
        pygame.draw.rect(display, (255, 150, 150), self.widen_phone_button_rect)
