import mouse
import sys
from time import sleep

if len(sys.argv) != 2:
    raise Exception("must pass in number of lootboxes to open")

num_lootboxes = int(sys.argv[1])
counter = 0
x_coord = 1711
y_coord = 1315

# wait for you to double click left click, and then starts the program
mouse.wait(button='right', target_types='double')
mouse.move(x_coord, y_coord, absolute=True)
while(counter < num_lootboxes):
    mouse.click(button='left')
    sleep(5.5)
    counter += 1
# print(mouse.get_position())

# mouse.click(button='right')