from states.state import *
class Launch_exit_state(State):
    def __init__(self, sys_settings):
        State.__init__(self, sys_settings)
        # standard phone state shit
        self.standard_phone_background = pygame.image.load("assets/standardMainSelection.png").convert_alpha()
        self.standard_phone_background = pygame.transform.scale(self.standard_phone_background, size)
        self.flippyphone_icon_rect = (360, 600, 100, 110)

        # blackfilter
        self.black_filter_alpha = 0
        self.black_filter = pygame.Surface(size)
        self.black_filter.fill((0, 0, 0))
        self.black_filter.set_alpha(self.black_filter_alpha)

    def update(self, click):
        self.black_filter_alpha += 5

        if (self.black_filter_alpha >= 255):
            self.black_filter_alpha = 255
            self.exit_state = 2

        self.black_filter.set_alpha(self.black_filter_alpha)

    def render(self, display):
        display.blit(self.standard_phone_background, (0, 0))
        display.blit(self.black_filter, (0, 0))
