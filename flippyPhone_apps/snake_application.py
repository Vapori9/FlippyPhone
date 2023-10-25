from flippyPhone_apps.flippyPhone_application import *
class Snake_application(FlippyPhone_application):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        FlippyPhone_application.__init__(self, sys_settings)

        self.snake = [[0,0]]
        self.snake_direction = 2


        self.timer_start_value = 15
        self.timer = self.timer_start_value




    def update(self, click):

        self.timer -= 1
        if (self.timer <= 0):
            self.timer = self.timer_start_value
            self.on_tick()



    def render(self, display):
        flippy_screen_draw_rect(self.snake[0][0]*16, self.snake[0][1]*16, 16, 16, 0, (0,150,0), display)



    def button_pressed(self, button_name):
        if (button_name == "RIGHT"):
            if (self.snake_direction != 4):
                self.snake_direction = 2

        if (button_name == "LEFT"):
            if (self.snake_direction != 2):
                self.snake_direction = 4

        if (button_name == "UP"):
            if (self.snake_direction != 3):
                self.snake_direction = 1

        if (button_name == "DOWN"):
            if (self.snake_direction != 1):
                self.snake_direction = 3

    def on_tick(self):
        # move the snake

        if (self.snake_direction == 1):
            self.snake[0][1] -= 1

        if (self.snake_direction == 2):
            self.snake[0][0] += 1

        if (self.snake_direction == 3):
            self.snake[0][1] += 1

        if (self.snake_direction == 4):
            self.snake[0][0] -= 1

