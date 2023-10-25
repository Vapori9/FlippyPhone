import os
from flippyPhone_apps.flippyPhone_application import *
class Music_application(FlippyPhone_application):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        FlippyPhone_application.__init__(self, sys_settings)
        self.pippeli = pygame.image.load("assets/pippeli_application/pippeli.png").convert_alpha()
        self.pippeli = pygame.transform.scale(self.pippeli, (self.pippeli.get_width() * 0.5, self.pippeli.get_height() * 0.5))


        self.exit_application = False
        self.names = os.listdir("music/")

        self.song_index = 0

        self.music_loaded = False


        self.current_song = None

        self.playing = False

        self.queen_sheet = pygame.image.load("assets/girl_sheet.png").convert_alpha()
        self.queen_current_image = pygame.Surface((85,138)).convert()
        self.girl_animation_index = 0





    def update(self, click):

        self.sheet_get_rect_with_pos(math.floor(self.girl_animation_index))

        self.girl_animation_index += 0.05 + self.playing*0.15


        if (not self.music_loaded):
            self.current_song = pygame.mixer.Sound("music/" + self.names[self.song_index])
            self.music_loaded = True

        if (self.girl_animation_index >= 8):
            self.girl_animation_index = 0



    def render(self, display):
        flippy_screen_draw_text(5, 330, 30, str(self.names[self.song_index]), display, (255, 255, 255))

        if (self.playing):
            flippy_screen_draw_text(5, 350, 30, "PLAYING", display, (0, 255, 150))
        else:
            flippy_screen_draw_text(5, 350, 30, "PAUSED", display, (255, 100, 0))

        flippy_screen_draw_image(200, 50, self.queen_current_image, display)




    def button_pressed(self, button_name):
        if (button_name == "DOWN"):
            self.playing = False
            self.current_song.stop()

            self.song_index += 1
            self.music_loaded = False
        elif (button_name == "UP"):
            self.playing = False
            self.current_song.stop()

            self.song_index -= 1
            self.music_loaded = False
        elif (button_name == "OK"):
            if (self.playing):
                self.current_song.stop()
            else:
                self.current_song.play()
            self.playing = not self.playing



        self.song_index = self.song_index % len(self.names)




    def sheet_get_rect_with_pos(self, index):
        self.queen_current_image = pygame.Surface((85,138)).convert()
        self.queen_current_image.blit(self.queen_sheet, (0 - index*85, 0))