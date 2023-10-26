# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the width and height of the screen [width, height]
size = (1.2*480, 1.2*800)

# The base resolution everything is thought to be in, the screen coordinates the objects position should be withing
# to be visible on the screen
base_size = (480, 800)

# A scale factor that is needed in calculations for the positions of objects if base_size != size
# RS = Resolution_Scale
RS = size[0] / base_size[0]
DISABLE_NOTIFICATIONS = False