from flippyPhone_apps.flippyPhone_application import *
class Notification_settings_application(FlippyPhone_application):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        FlippyPhone_application.__init__(self, sys_settings)
        self.pippeli = pygame.image.load("assets/pippeli_application/pippeli.png").convert_alpha()
        self.pippeli = pygame.transform.scale(self.pippeli, (self.pippeli.get_width() * 0.5, self.pippeli.get_height() * 0.5))

        self.cursor = [0, 0]
        self.cursor_dimensions = [1, 3]

        # SETTINGS





    def update(self, click):
        pass


    def render(self, display):
        #flippy_screen_draw_image(200, 200, self.pippeli, display)

        # Notifications setting
        flippy_screen_draw_text(50, 32, 30, "Filtered Notifications", display, (255,255,255))
        flippy_screen_draw_rect(300, 32, 50, 20, 0, (0, 255, 255), display)
        flippy_screen_draw_rect(305, 34, 15 + self.system_settings.disable_notifications*25, 16, 0, (255, 255, 50), display)

        # Supa secret1 setting
        flippy_screen_draw_text(50, 32 + 40, 30, "Super Secret", display, (255, 255, 255))
        flippy_screen_draw_rect(300, 32 + 40, 50, 20, 0, (0, 255, 255), display)
        flippy_screen_draw_rect(305, 34 + 40, 15 + self.system_settings.super_secret * 25, 16, 0, (255, 255, 50), display)

        # Supa secret2 setting
        flippy_screen_draw_text(50, 32 + 40*2, 30, "Super Secret 2", display, (255, 255, 255))
        flippy_screen_draw_rect(300, 32 + 40*2, 50, 20, 0, (0, 255, 255), display)
        flippy_screen_draw_rect(305, 34 + 40*2, 15 + self.system_settings.super_secret2 * 25, 16, 0, (255, 255, 50), display)





        # cursor
        flippy_screen_draw_circle(20, 40 + 40 * self.cursor[1], 5, (150,30,80), display)




    def button_pressed(self, button_name):
        if (button_name == "DOWN"):
            self.cursor[1] += 1
        elif (button_name == "UP"):
            self.cursor[1] -= 1

        elif (button_name == "OK"):
            if (self.cursor[1] == 0):
                self.system_settings.disable_notifications = not self.system_settings.disable_notifications

            if (self.cursor[1] == 1):
                self.system_settings.super_secret = not self.system_settings.super_secret

            if (self.cursor[1] == 2):
                self.system_settings.super_secret2 = not self.system_settings.super_secret2


        self.cursor_logic()

    def cursor_logic(self):
        self.cursor[0] = self.cursor[0] % self.cursor_dimensions[0]
        self.cursor[1] = self.cursor[1] % self.cursor_dimensions[1]



