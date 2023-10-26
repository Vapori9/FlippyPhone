import random

from flippyPhone_apps.flippyPhone_application import *
class Snake_application(FlippyPhone_application):
    # initialization
    def __init__(self, sys_settings):
        # initialize parent
        FlippyPhone_application.__init__(self, sys_settings)

        head = self.Pos(0,0)
        self.snake = [head]
        self.snake_direction = 2


        self.timer_start_value = 15
        self.timer = self.timer_start_value

        self.ate_thing = False
        self.food = self.Pos(random.randint(1,25), random.randint(1,20))

        self.direction_set_this_tick = False

        self.bruh_sound = pygame.mixer.Sound("sounds/augh.wav")
        self.chomp_sound = pygame.mixer.Sound("sounds/chomp.wav")




    def update(self, click):

        self.timer -= 1
        if (self.timer <= 0):
            self.timer = self.timer_start_value
            self.on_tick()



    def render(self, display):
        index = 0
        for i in self.snake:
            color = (0, 150, 0)
            if (index == 0):
                color = (50, 150, 150)
            flippy_screen_draw_rect(i.x*16, i.y*16, 16, 16, 0, color, display)
            index += 1

        flippy_screen_draw_rect(self.food.x * 16, self.food.y * 16, 16, 16, 0, (255, 0, 0), display)
        flippy_screen_draw_text(160, 10, 24, "POINTS:" + str(len(self.snake) - 1), display, (150, 150, 150))



    def button_pressed(self, button_name):


        if (self.direction_set_this_tick):
            return

        self.direction_set_this_tick = True



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
        self.direction_set_this_tick = False
        self.ate_thing = False



        tail = self.Pos(self.snake[len(self.snake)-1].x, self.snake[len(self.snake)-1].y)
        # move snake parts
        for i in reversed(range(1, len(self.snake))):
            self.snake[i] = self.Pos(self.snake[i-1].x, self.snake[i-1].y)



        # move the snake head
        if (self.snake_direction == 1):
            self.snake[0].y -= 1

        if (self.snake_direction == 2):
            self.snake[0].x += 1

        if (self.snake_direction == 3):
            self.snake[0].y += 1

        if (self.snake_direction == 4):
            self.snake[0].x -= 1

        if (self.collides_with_body()):
            self.reset()
            return

        if (self.is_outside_of_bounds()):
            self.reset()
            return


        if (self.snake[0].x == self.food.x and self.snake[0].y == self.food.y):
            self.chomp_sound.play()
            self.ate_thing = True
            self.food = self.Pos(random.randint(1,25), random.randint(1,20))

        if (self.ate_thing):
            self.snake.append(tail)

    def is_outside_of_bounds(self):
        if (self.snake[0].x < 1):
            return True

        if (self.snake[0].x > 27):
            return True

        if (self.snake[0].y < 0):
            return True

        if (self.snake[0].y > 22):
            return True

        return False


    def collides_with_body(self):
        value = False

        for i in (range(1, len(self.snake))):
            if (self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y):
                value = True

        return value

    def reset(self):
        self.bruh_sound.play()
        head = self.Pos(0, 0)
        self.snake = [head]
        self.snake_direction = 2

        self.timer_start_value = 15
        self.timer = self.timer_start_value

        self.ate_thing = False
        self.food = self.Pos(random.randint(1,25), random.randint(1,20))


    class Pos:
        def __init__(self, x, y):
            self.x = x
            self.y = y

