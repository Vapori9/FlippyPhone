from flippyPhone_apps.flippyPhone_application import *
class Messages_application(FlippyPhone_application):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        FlippyPhone_application.__init__(self, sys_settings)
        self.pippeli = pygame.image.load("assets/road_work_ahead.png").convert_alpha()
        self.pippeli = pygame.transform.scale(self.pippeli, (self.pippeli.get_width() * 0.6, self.pippeli.get_height() * 0.5))




    def update(self, click):
        pass


    def render(self, display):
        flippy_screen_draw_image(0, 50, self.pippeli, display)
        flippy_screen_draw_text(20, 20, 24, "Sorry this app is under construction :(", display, (255,255,255))



