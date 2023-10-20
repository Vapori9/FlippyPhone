import pygame
from settings import *
from functions import *

# A parent class for different states of the program, instances of this class necessary don't do anything
class State:
    def __init__(self):
        # a variable that tells the application when the current states is asking to change to some
        # different state, if exit_state = -1, do nothing, if exit_state = 0, go to state valued at 0 etc.
        self.exit_state = -1

    def update(self, click):
        pass

    def render(self, display):
        pass

    def get_exit_state_value(self):
        # If exit_state != -1 then we save its current value
        temporary = self.exit_state

        # The state will now exit after returning the not -1 value to the application but the exit state is still at
        # some other value than -1
        # So we must reset the exit value so this state won't exit immediately after this state is set the next time
        self.exit_state = -1

        # return the value
        return temporary