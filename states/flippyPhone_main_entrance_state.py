from states.state import *
class FlippyPhone_main_entrance_state(State):
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


    def update(self, click):
        self.black_filter_alpha -= 5
        if (self.black_filter_alpha <= 0):
            self.black_filter_alpha = 0
            self.exit_state = 3
        self.black_filter.set_alpha(self.black_filter_alpha)

    def render(self, display):
        display.blit(self.flippyphone_closed_image, (size[0] / 2 - size[0] / 4, size[1] / 2))
        display.blit(self.black_filter, (0, 0))