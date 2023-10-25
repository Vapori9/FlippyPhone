import os
from flippyPhone_apps.flippyPhone_application import *
class Gallery_application(FlippyPhone_application):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        FlippyPhone_application.__init__(self, sys_settings)
        self.pippeli = pygame.image.load("assets/pippeli_application/pippeli.png").convert_alpha()
        self.pippeli = pygame.transform.scale(self.pippeli, (self.pippeli.get_width() * 0.5, self.pippeli.get_height() * 0.5))

        self.exit_application = False
        self.names = os.listdir("gallery_images/")

        self.image_index = 0

        self.image_loaded = False

        self.current_image = pygame.image.load("gallery_images/" + str(self.names[0])).convert()





    def update(self, click):
        if (not self.image_loaded):
            self.current_image = pygame.image.load("gallery_images/" + str(self.names[self.image_index])).convert()
            if (self.current_image.get_width() >= self.current_image.get_height()):
                scale = self.current_image.get_height()*1.0/self.current_image.get_width()
                new_width = 400
                new_height = 400*scale
                self.current_image = pygame.transform.scale(self.current_image, (new_width, new_height))
            else:
                scale = self.current_image.get_width() * 1.0 / self.current_image.get_height()
                new_width = 400 * scale
                new_height = 400
                self.current_image = pygame.transform.scale(self.current_image, (new_width, new_height))

            self.image_loaded = True



    def render(self, display):
        display.blit(self.current_image, (40, 0))
        flippy_screen_draw_text(5, 350, 30, str(self.names[self.image_index]), display, (255, 255, 255))


    def button_pressed(self, button_name):
        if (button_name == "DOWN"):
            self.image_index += 1
            self.image_loaded = False
        elif (button_name == "UP"):
            self.image_index -= 1
            self.image_loaded = False

        print(self.image_index)
        self.image_index = self.image_index % len(self.names)


