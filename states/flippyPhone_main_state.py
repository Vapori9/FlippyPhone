from states.state import *

class FlippyPhone_main_state(State):
    def __init__(self):
        State.__init__(self)


        # Flippyphone opened
        self.flippyPhone_opened_image = pygame.image.load("assets/flippyOpened.png")
        self.flippyPhone_opened_image = pygame.transform.scale(self.flippyPhone_opened_image,
                                                               ((int(size[0] / 2)), size[1]))

        self.close_phone_button_rect = (RS*170, RS*5, RS*135, RS*30)

        self.widen_phone_button_rect = (RS*10, RS*600, RS*30, RS*120)

    def update(self, click):
        if (click != None):
            clickRect = (click[0], click[1], 2, 2)
            if (rectCollision(self.close_phone_button_rect, clickRect)):
                self.exit_state = 3

            if (rectCollision(self.widen_phone_button_rect, clickRect)):
                self.exit_state = 5

    def render(self, display):
        display.blit(self.flippyPhone_opened_image, (size[0] / 2 - size[0] / 4, 0))
        pygame.draw.rect(display, (0, 150, 200), self.close_phone_button_rect)
        pygame.draw.rect(display, (255, 150, 150), self.widen_phone_button_rect)
