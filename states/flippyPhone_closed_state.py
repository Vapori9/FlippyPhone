from states.state import *

class FlippyPhone_closed_state(State):
    def __init__(self, sys_settings):
        State.__init__(self, sys_settings)

        # blackfilter
        self.black_filter_alpha = 0
        self.black_filter = pygame.Surface(size)
        self.black_filter.fill((0, 0, 0))
        self.black_filter.set_alpha(self.black_filter_alpha)

        # Flippyphone closed
        self.flippyphone_closed_image = pygame.image.load("assets/flippyClosed.png")
        self.flippyphone_closed_image = pygame.transform.scale(self.flippyphone_closed_image,
                                                               ((int(size[0] / 2)), int(size[1] / 2)))

        self.open_phone_button_rect = (0, size[1]*0.06, size[0], size[1]*0.94)

        self.exit_button_rect = (0, size[1]*0.95, size[0]*0.1,size[1]*0.05)

        self.open_sound = pygame.mixer.Sound("sounds/open_flap.wav")


    def update(self, click):
        if (click != None):
            clickRect = (click[0], click[1], 2, 2)
            if (rectCollision(self.open_phone_button_rect, clickRect)):
                self.exit_state = 4
                self.open_sound.play()

            if (rectCollision(self.exit_button_rect, clickRect)):
                self.exit_state = 0
                self.system_settings.disable_notifications = False

    def render(self, display):
        display.blit(self.flippyphone_closed_image, (size[0] / 2 - size[0] / 4, size[1] / 2))
        display.blit(self.flippyphone_closed_image, (size[0] / 2 - size[0] / 4, size[1] / 2))
        pygame.draw.rect(display, (255, 100, 100), self.exit_button_rect)