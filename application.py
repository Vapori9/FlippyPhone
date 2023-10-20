import pygame
from settings import *
from functions import rectCollision

from states.launch_state import *
from states.launch_exit_state import *
from states.flippyPhone_main_entrance_state import *
from states.flippyPhone_closed_state import *
from states.flippyPhone_main_state import *
from states.flippyPhone_main_selection_state import *

class Application:
    def __init__(self):
        # All the global data needed for each of the different states

        # Initializing all of the states, all of them are currently loaded in memory but I guess that for the
        # scope of this project it's fine
        self.launch_state = Launch_state()
        self.launch_exit_state = Launch_exit_state()

        self.flippyPhone_main_entrance_state = FlippyPhone_main_entrance_state()
        self.flippyPhone_closed_state = FlippyPhone_closed_state()
        self.flippyPhone_main_state = FlippyPhone_main_state()
        self.flippyPhone_main_selection_state = FlippyPhone_main_selection_state()


        # A dictionary from number to its corresponding state inherited child instance
        self.states = {0 : self.launch_state,
                       1 : self.launch_exit_state,
                       2 : self.flippyPhone_main_entrance_state,
                       3 : self.flippyPhone_closed_state,
                       4 : self.flippyPhone_main_state,
                       5 : self.flippyPhone_main_selection_state}
        # Set the initial state
        self.state = 0

    # Update at least the current states requested things
    def update(self, click):
        self.states[self.state].update(click)



        exit_state = self.states[self.state].get_exit_state_value()
        if (exit_state != -1):
            self.state = exit_state

    # Render at least the contents of the current state
    def render(self, display):
        self.states[self.state].render(display)

        # Of course it is possible to render here something on top of the drawn image, notifications for example

        # like this comment away when not needed
        #pygame.draw.rect(display, (0, 50 ,255), ((1/10) * size[0], 0, (8/10) * size[0], (2/10) * size[1]), 0)










