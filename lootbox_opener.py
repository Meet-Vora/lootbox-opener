import mouse
import sys
from time import sleep

if len(sys.argv) != 3:
    raise Exception("must pass in number of lootboxes to open")

num_lootboxes = sys.argv[2]
counter = 0
# wait for you to double click left click, and then starts the program
mouse.wait(button='right', target_types='double')
mouse.move(1711, 1315, absolute=True)
while(counter < num_lootboxes)
    mouse.click(button='left')
    sleep(5)
    counter += 1
# print(mouse.get_position())

# mouse.click(button='right')