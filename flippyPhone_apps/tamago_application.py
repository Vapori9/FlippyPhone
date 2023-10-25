
from flippyPhone_apps.flippyPhone_application import *
class Tamago_application(FlippyPhone_application):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        FlippyPhone_application.__init__(self, sys_settings)
        self.pippeli = pygame.image.load("assets/tamago_application/egg.png").convert_alpha()
        self.pippeli = pygame.transform.scale(self.pippeli, (self.pippeli.get_width() * 2, self.pippeli.get_height() * 2))
        self.bruh_sound = pygame.mixer.Sound("sounds/bruh.wav")
        self.count = 100000




    def update(self, click):
        pass


    def render(self, display):
        flippy_screen_draw_image(140, 150, self.pippeli, display)
        flippy_screen_draw_text(140, 20, 30, str(self.count), display, (100, 150, 255))

    def button_pressed(self, button_name):
        if (button_name == "OK"):
            self.count -= 1
            self.bruh_sound.play()



