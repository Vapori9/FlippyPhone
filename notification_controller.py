import pygame, random, math
from settings import *
class NotificationController:
    def __init__(self, sys_settings):

        self.system_settings = sys_settings

        self.notifications = []
        self.notification_sound = pygame.mixer.Sound("sounds/notification.wav")

        self.notification_min_interval = 300 # 5 seconds
        self.last_notification_value = -1

        self.important_notification_timer = random.randint(0.5*60*60, 2*60*60)
        self.important_notification_played = False







    def updade(self):
        for i in self.notifications:
            i.update()

        if (self.notification_min_interval > 0):
            self.notification_min_interval -= 1


        if (random.randint(0, 400) == 0 and self.notification_min_interval <= 0 and self.system_settings.disable_notifications == False):
            self.notification_min_interval = 300
            notification_value = random.randint(0,13)

            temp = notification_value
            if (temp == self.last_notification_value):
                notification_value += 1
            self.last_notification_value = temp
            if (notification_value == 0):
                self.spawn_notification("Snapchat", "assets/notification_icons/snapchat_icon.png",
                                    "Jorma Seisova lähetti sinulle chatin")
            elif (notification_value == 1):
                self.spawn_notification("Mobilepay", "assets/notification_icons/mobilepay_icon.png",
                                        "Janne Nakki  lähetti sinulle 5 euroa rahaa :)")

            elif (notification_value == 2):
                self.spawn_notification("Snapchat", "assets/notification_icons/snapchat_icon.png",
                                        "Marjatta lähetti sinulle Snapin")

            elif (notification_value == 3):
                self.spawn_notification("Snapchat", "assets/notification_icons/snapchat_icon.png",
                                        "Alvar:D lisäsi tarinaansa")

            elif (notification_value == 4):
                self.spawn_notification("Snapchat", "assets/notification_icons/snapchat_icon.png",
                                        "Bruhman15 lisäsi sinut kaverikseen")

            elif (notification_value == 5):
                self.spawn_notification("Telegram", "assets/notification_icons/telegram_icon.png",
                                        "Käyttistä: Eemeli lähetti kuvan")

            elif (notification_value == 6):
                self.spawn_notification("Clash Royale", "assets/notification_icons/clashRoyale_icon.png",
                                        "Hups unohdit avata laatikon :(")

            elif (notification_value == 7):
                self.spawn_notification("My Gallery", "assets/notification_icons/donkey_icon.png",
                                        "Käy katsomassa uudet tuoreet julkaisut")

            elif (notification_value == 8):
                self.spawn_notification("messages-noreply", "assets/notification_icons/gmail_icon.png",
                                        "Ehdit vielä antaa palautetta kurssista NBE-C2102")

            elif (notification_value == 9):
                self.spawn_notification("Youtube", "assets/notification_icons/youtube_icon.png",
                                        "niilo22 - Kiitos lahkotuksesta", "assets/niilo22.png", (255, 0, 0))

            elif (notification_value == 10):
                self.spawn_notification("WhatsApp \n Jarmo Ilkkala", "assets/notification_icons/whatsApp_icon.png",
                                        "Millane päivä sulla on huomenna", "assets/notification_icons/mies_kuva.png")
            elif (notification_value == 11):
                self.spawn_notification("Snapchat", "assets/notification_icons/snapchat_icon.png",
                                        "Timppa Ahopelto lähetti sinulle Snapin")

            elif (notification_value == 12):
                self.spawn_notification("WhatsApp \n Pentti", "assets/notification_icons/whatsApp_icon.png",
                                        "Et oo koskaan tehny noin", "assets/notification_icons/pentti_kuva.png")
        if (self.system_settings.disable_notifications == True):

            if (self.important_notification_timer > 0):
                self.important_notification_timer -= 1
            elif (self.important_notification_played == False):
                self.important_notification_played = True
                self.spawn_notification("Messages\n Olli-kaveri", "assets/notification_icons/messages_icon.png",
                                        "Moi, ovikoodi on 6471")



    def get_notifications(self):
        return self.notifications

    def spawn_notification(self, app_name, icon_path, info, additional_pic=None, titleColor=(0, 0, 0)):
        self.notifications.append(Notification(app_name, icon_path, info, additional_pic, titleColor))
        self.notification_sound.play()






class Notification:
    def __init__(self, app_name, icon_path, info, additional_pic=None, titleColor=(0, 0, 0)):
        self.appname = app_name
        self.icon_path = icon_path
        self.info = info


        self.appear_timer = 50
        self.appear_timer_max = 50

        self.display_timer = 600
        self.display_timer_max = 600

        self.disappear_timer = 50
        self.disappear_timer_max = 50


        self.y_coord = 0

        self.surface = pygame.surface.Surface((size[0], size[1]*0.14))
        self.surface.fill((255, 255, 255))
        self.surface.set_alpha(200)


        # Draw the icon of the notification
        self.icon_surface = pygame.image.load(icon_path).convert_alpha()
        self.icon_surface = pygame.transform.scale(self.icon_surface, (80*RS, 80*RS))
        self.surface.blit(self.icon_surface, (RS*15, RS*20))

        # Draw the text naming the application the notification is from
        self.font = pygame.font.SysFont(None, math.ceil(22*RS))
        self.name_text = self.font.render(app_name, True, titleColor)
        self.surface.blit(self.name_text, (RS*100, RS*20))

        self.info_text = self.font.render(info, True, (0,0,0))
        self.surface.blit(self.info_text, (RS*110, RS*60))

        if (additional_pic != None):
            self.additional_icon_surface = pygame.image.load(additional_pic).convert_alpha()
            self.additional_icon_surface = pygame.transform.scale(self.additional_icon_surface, (80 * RS, 70 * RS))
            self.surface.blit(self.additional_icon_surface, (RS * 360, RS * 40))


    def update(self):
        if (self.appear_timer > 0):
            self.y_coord = -1*size[1]*0.2 * (self.appear_timer * 1.0 / self.appear_timer_max)
            print(self.appear_timer)
            self.appear_timer -= 1.5

        elif (self.display_timer > 0):
            self.y_coord = 0
            self.display_timer -= 1.5

        elif (self.disappear_timer > 0):
            self.y_coord = -size[1] * 0.2 + 1 * size[1] * 0.2 * (self.disappear_timer * 1.0 / self.disappear_timer_max)
            self.disappear_timer -= 1.5

    def render(self): # returns a pygame.surface
        return self.surface

    def get_y_coord(self):
        return self.y_coord

    def get_played(self):
        return self.display_timer < 0
