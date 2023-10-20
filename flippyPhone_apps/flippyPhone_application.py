import pygame
from settings import *
from functions import *

# A parent class for different states of the program, instances of this class necessary don't do anything
class FlippyPhone_application:
    def __init__(self):
        # a variable that tells the application when the current states is asking to change to some
        # different state, if exit_state = -1, do nothing, if exit_state = 0, go to state valued at 0 etc.
        self.exit_application = False

    def update(self, click):
        pass

    def render(self, display):
        pass

    def get_exit_state_value(self):
        temporary = self.exit_application

        # set the exit bool to false so the app won't exit immediately when opened again
        self.exit_application = False

        # return the value
        return temporary