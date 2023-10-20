from flippyPhone_apps.flippyPhone_application import *
class Pippeli_application(FlippyPhone_application):
    # initialization
    def __init__(self):
        # initialize parent
        FlippyPhone_application.__init__(self)
        self.pippeli = pygame.image.load("assets/pippeli_application/pippeli.png").convert_alpha()
        self.pippeli = pygame.transform.scale(self.pippeli, (self.pippeli.get_width() * 0.5, self.pippeli.get_height() * 0.5))




    def update(self, click):
        pass


    def render(self, display):
        flippy_screen_draw_image(200, 200, self.pippeli, display)



