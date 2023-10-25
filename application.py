import pygame
from settings import *
from functions import rectCollision

from states.launch_state import *
from states.launch_exit_state import *
from states.flippyPhone_main_entrance_state import *
from states.flippyPhone_closed_state import *
from states.flippyPhone_main_state import *
from states.flippyPhone_main_selection_state import *

from system_settings import *
from notification_controller import *

class Application:
    def __init__(self):

        self.system_settings = System_settings()

        # All the global data needed for each of the different states

        # Initializing all of the states, all of them are currently loaded in memory but I guess that for the
        # scope of this project it's fine
        self.launch_state = Launch_state(self.system_settings)
        self.launch_exit_state = Launch_exit_state(self.system_settings)

        self.flippyPhone_main_entrance_state = FlippyPhone_main_entrance_state(self.system_settings)
        self.flippyPhone_closed_state = FlippyPhone_closed_state(self.system_settings)
        self.flippyPhone_main_state = FlippyPhone_main_state(self.system_settings)
        self.flippyPhone_main_selection_state = FlippyPhone_main_selection_state(self.system_settings)



        # A dictionary from number to its corresponding state inherited child instance
        self.states = {0 : self.launch_state,
                       1 : self.launch_exit_state,
                       2 : self.flippyPhone_main_entrance_state,
                       3 : self.flippyPhone_closed_state,
                       4 : self.flippyPhone_main_state,
                       5 : self.flippyPhone_main_selection_state}
        # Set the initial state
        self.state = 0





        self.notification_controller = NotificationController(self.system_settings)


    # Update at least the current states requested things
    def update(self, click):
        self.states[self.state].update(click)

        self.notification_controller.updade()


        exit_state = self.states[self.state].get_exit_state_value()
        if (exit_state != -1):
            self.state = exit_state

    # Render at least the contents of the current state
    def render(self, display):
        self.states[self.state].render(display)

        notifications = self.notification_controller.get_notifications()
        if (len(notifications) > 0):
            reversed_notifications = notifications[::-1]
            notification = reversed_notifications[0]
            display.blit(notification.render(), (0, notification.get_y_coord()))

        # Of course it is possible to render here something on top of the drawn image, notifications for example












