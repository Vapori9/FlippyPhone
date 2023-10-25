from states.state import *

from flippyPhone_apps.pippeli_application import *
from flippyPhone_apps.tamago_application import *
from flippyPhone_apps.notification_settings_application import *
from flippyPhone_apps.gallery_application import *
from flippyPhone_apps.music_application import *
from flippyPhone_apps.snake_application import *
class FlippyPhone_main_selection_state(State):
    def __init__(self, sys_settings):
        State.__init__(self, sys_settings)


        self.snake_application = Snake_application(self.system_settings)


        self.notification_settings_application = Notification_settings_application(self.system_settings)

        self.gallery_application = Gallery_application(self.system_settings)

        self.music_application = Music_application(self.system_settings)

        self.tamago_application = Tamago_application(self.system_settings)

        # map From int -> FlippyPhone application like for example settings, snake game or some shit
        # 0 means there is no application running
        self.flippyPhone_applications = {
            0: None,
            1: self.snake_application,
            2: self.notification_settings_application,
            3: None,
            4: self.gallery_application,
            5: self.music_application,
            6: self.tamago_application
        }
        self.current_application_index = 0

        self.cursor = [0, 0]
        self.cursorDimension = [3, 2]



        # Loading necessary assets
        self.flippyPhone_screen_image = pygame.image.load("assets/flippyScreen.png")
        self.flippyPhone_screen_image = pygame.transform.scale(self.flippyPhone_screen_image,
                                                               ((int(size[0])), size[1] / 2))
        self.flippyPhone_keyboard_image = pygame.image.load("assets/flippyKeyboard.png")
        self.flippyPhone_keyboard_image = pygame.transform.scale(self.flippyPhone_keyboard_image,
                                                                 ((int(size[0])), size[1] / 2))


        # Download all the images that are needed here so they arent downloaded all around the code
        # downloading and scaling if wanted can be done the following way
        self.background = pygame.image.load("assets/frutiger_background.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.background.get_width()*0.20, self.background.get_height()*0.13))


        # Load all application icon images
        self.snake_application_icon = pygame.image.load("assets/flippyphone_app_icons/snake_app_icon.png").convert_alpha()
        self.snake_application_icon = pygame.transform.scale(self.snake_application_icon, (
        self.snake_application_icon.get_width() * 1, self.snake_application_icon.get_height() * 1))

        self.settings_application_icon = pygame.image.load(
            "assets/flippyphone_app_icons/settings_app_icon.png").convert_alpha()
        self.settings_application_icon = pygame.transform.scale(self.settings_application_icon, (
            self.settings_application_icon.get_width() * 1, self.settings_application_icon.get_height() * 1))

        self.messages_application_icon = pygame.image.load(
            "assets/flippyphone_app_icons/messages_app_icon.png").convert_alpha()
        self.messages_application_icon = pygame.transform.scale(self.messages_application_icon, (
            self.messages_application_icon.get_width() * 1, self.messages_application_icon.get_height() * 1))

        self.gallery_application_icon = pygame.image.load(
            "assets/flippyphone_app_icons/gallery_app_icon.png").convert_alpha()
        self.gallery_application_icon = pygame.transform.scale(self.gallery_application_icon, (
            self.gallery_application_icon.get_width() * 1, self.gallery_application_icon.get_height() * 1))

        self.music_application_icon = pygame.image.load(
            "assets/flippyphone_app_icons/music_app_icon.png").convert_alpha()
        self.music_application_icon = pygame.transform.scale(self.music_application_icon, (
            self.music_application_icon.get_width() * 1, self.music_application_icon.get_height() * 1))

        self.tamago_application_icon = pygame.image.load(
            "assets/flippyphone_app_icons/tamago_app_icon.png").convert_alpha()
        self.tamago_application_icon = pygame.transform.scale(self.tamago_application_icon, (
            self.tamago_application_icon.get_width() * 1, self.tamago_application_icon.get_height() * 1))





        self.button_OK_rect = (RS * 217, RS * 445, RS * 55, RS * 50)

        self.button_LEFT_rect = (RS * 155, RS * 440, RS * 35, RS * 60)

        self.button_RIGHT_rect = (RS * 295, RS * 440, RS * 35, RS * 60)

        self.button_UP_rect = (RS * 220, RS * 400, RS * 50, RS * 35)

        self.button_DOWN_rect = (RS * 220, RS * 500, RS * 50, RS * 35)




        self.tighten_phone_button_rect = (RS*345, RS*470, RS*80, RS*70)



    def update(self, click):

        # First of all check if some flippyPhone application (for example snake is running)
        if (self.current_application_index != 0):

            # check if the user wants to exit the flippy application
            if (click != None):
                clickRect = (click[0], click[1], 2, 2)
                if (rectCollision(self.tighten_phone_button_rect, clickRect)):
                    self.current_application_index = 0
                    return

                if (rectCollision(self.button_OK_rect, clickRect)):
                    self.flippyPhone_applications[self.current_application_index].button_pressed("OK")

                elif (rectCollision(self.button_RIGHT_rect, clickRect)):
                    self.flippyPhone_applications[self.current_application_index].button_pressed("RIGHT")

                elif (rectCollision(self.button_LEFT_rect, clickRect)):
                    self.flippyPhone_applications[self.current_application_index].button_pressed("LEFT")

                elif (rectCollision(self.button_DOWN_rect, clickRect)):
                    self.flippyPhone_applications[self.current_application_index].button_pressed("DOWN")

                elif (rectCollision(self.button_UP_rect, clickRect)):
                    self.flippyPhone_applications[self.current_application_index].button_pressed("UP")


            # update the running application
            self.flippyPhone_applications[self.current_application_index].update(click)

            # exit from this function because no other changes must not be made
            return


        # update this state otherwise

        # check clicks
        if (click != None):
            clickRect = (click[0], click[1], 2, 2)

            self.keyboard_logic(clickRect)




    def render(self, display):
        if (self.current_application_index != 0):
            # draw the running application
            self.flippyPhone_applications[self.current_application_index].render(display)

        # else draw the states selection interface
        else:
            # Do the drawing using the functions provided in the functions.py file
            flippy_screen_draw_image(0, 0, self.background, display)

            # Draw the application icons
            self.draw_application_icons(display)

            # draw the cursor
            flippy_screen_draw_circle(60 + self.cursor[0]*165, 60 + self.cursor[1]*130, 40, (150,50,50),  display, 5)

        # everything that is not under the screen will be covered byt the keyboard and the screen
        display.blit(self.flippyPhone_screen_image, (0, 0))
        display.blit(self.flippyPhone_keyboard_image, (0, size[1] / 2))


        pygame.draw.rect(display, (0, 150, 200), self.button_OK_rect)

        pygame.draw.rect(display, (0, 150, 0), self.button_UP_rect)
        pygame.draw.rect(display, (0, 150, 0), self.button_DOWN_rect)
        pygame.draw.rect(display, (0, 150, 0), self.button_LEFT_rect)
        pygame.draw.rect(display, (0, 150, 0), self.button_RIGHT_rect)

        pygame.draw.rect(display, (255, 100, 100), self.tighten_phone_button_rect)



    # Write additional function here, don't write any play code to the update method to keep things clear, use functions
    # |
    # V

    def keyboard_logic(self, clickRect):
        if (rectCollision(self.button_OK_rect, clickRect)):
            self.OK_button_logic()
        elif (rectCollision(self.button_RIGHT_rect, clickRect)):
            self.cursor[0] += 1

        elif (rectCollision(self.button_LEFT_rect, clickRect)):
            self.cursor[0] -= 1

        elif (rectCollision(self.button_DOWN_rect, clickRect)):
            self.cursor[1] += 1

        elif (rectCollision(self.button_UP_rect, clickRect)):
            self.cursor[1] -= 1

        elif (rectCollision(self.tighten_phone_button_rect, clickRect)):
            self.exit_state = 4



        self.cursor_logic()


    def cursor_logic(self):
        self.cursor[0] = self.cursor[0] % self.cursorDimension[0]
        self.cursor[1] = self.cursor[1] % self.cursorDimension[1]

    def OK_button_logic(self):

        if (self.cursor == [0,0]):
            self.current_application_index = 1

        if (self.cursor == [1,0]):
            self.current_application_index = 2

        if (self.cursor == [0,1]):
            self.current_application_index = 4

        if (self.cursor == [1,1]):
            self.current_application_index = 5

        if (self.cursor == [2,1]):
            self.current_application_index = 6

    def draw_application_icons(self, display):
        flippy_screen_draw_image(20, 20, self.snake_application_icon, display)
        flippy_screen_draw_text(24, 100, 24, "Snake", display, (20,20,20))

        flippy_screen_draw_image(20 + 165, 20, self.settings_application_icon, display)
        flippy_screen_draw_text(20 + 165, 100, 24, "Notification", display, (20, 20, 20))
        flippy_screen_draw_text(28 + 165, 120, 24, "Settings", display, (20, 20, 20))

        flippy_screen_draw_image(20 + 165*2, 20, self.messages_application_icon, display)
        flippy_screen_draw_text(20 + 165*2, 100, 24, "Messages", display, (20, 20, 20))

        flippy_screen_draw_image(20, 20 + 130*1, self.gallery_application_icon, display)
        flippy_screen_draw_text(28, 100 + 130*1, 24, "Gallery", display, (20, 20, 20))

        flippy_screen_draw_image(20 + 165*1, 20 + 130 * 1, self.music_application_icon, display)
        flippy_screen_draw_text(36 + 165*1, 100 + 130 * 1, 24, "Music", display, (20, 20, 20))

        flippy_screen_draw_image(20 + 165 * 2, 20 + 130 * 1, self.tamago_application_icon, display)
        flippy_screen_draw_text(36 + 165 * 2, 100 + 130 * 1, 24, "Tamago", display, (20, 20, 20))




