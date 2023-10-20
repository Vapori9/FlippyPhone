from states.state import *

from flippyPhone_apps.pippeli_application import *
class FlippyPhone_main_selection_state(State):
    def __init__(self):
        State.__init__(self)


        self.pippeli_application = Pippeli_application()
        # map From int -> FlippyPhone application like for example settings, snake game or some shit
        # 0 means there is no application running
        self.flippyPhone_applications = {
            0: None,
            1: self.pippeli_application
        }
        self.current_application_index = 0



        # Loading necessary assets
        self.flippyPhone_screen_image = pygame.image.load("assets/flippyScreen.png")
        self.flippyPhone_screen_image = pygame.transform.scale(self.flippyPhone_screen_image,
                                                               ((int(size[0])), size[1] / 2))
        self.flippyPhone_keyboard_image = pygame.image.load("assets/flippyKeyboard.png")
        self.flippyPhone_keyboard_image = pygame.transform.scale(self.flippyPhone_keyboard_image,
                                                                 ((int(size[0])), size[1] / 2))


        # Download all the images that are needed here so they arent downloaded all around the code
        # downloading and scaling if wanted can be done the following way
        self.es = pygame.image.load("assets/es.png").convert_alpha()
        self.es = pygame.transform.scale(self.es, (self.es.get_width()*0.5, self.es.get_height()*0.5))

        self.button_OK_rect = (RS * 217, RS * 445, RS * 50, RS * 50)
        self.tighten_phone_button_rect = (RS*10, RS*600, RS*30, RS*120)



    def update(self, click):

        # First of all check if some flippyPhone application (for example snake is running)
        if (self.current_application_index != 0):
            # update the running application
            self.flippyPhone_applications[self.current_application_index].update(click)

            # exit from this function because no other changes must not be made
            return


        # update this state otherwise

        # check clicks
        if (click != None):
            clickRect = (click[0], click[1], 2, 2)
            if (rectCollision(self.button_OK_rect, clickRect)):
                self.current_application_index = 1
            elif (rectCollision(self.tighten_phone_button_rect, clickRect)):
                self.exit_state = 4





    def render(self, display):
        if (self.current_application_index != 0):
            # draw the running application
            self.flippyPhone_applications[self.current_application_index].render(display)

        # else draw the states selection interface
        else:
            # Do the drawing using the functions provided in the functions.py file
            flippy_screen_draw_rect(300, 50, 20, 20, 0, (0, 255, 0), display)
            flippy_screen_draw_circle(100, 100, 20, (0, 0, 255), display)
            flippy_screen_draw_image(200, 200, self.es, display)

        # everything that is not under the screen will be covered byt the keyboard and the screen
        display.blit(self.flippyPhone_screen_image, (0, 0))
        display.blit(self.flippyPhone_keyboard_image, (0, size[1] / 2))

        pygame.draw.rect(display, (0, 150, 200), self.button_OK_rect)
        pygame.draw.rect(display, (255, 150, 150), self.tighten_phone_button_rect)



    # Write additional function here, don't write any play code to the update method to keep things clear, use functions
    # |
    # V
