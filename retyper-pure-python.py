

import time

# python3 -m pip install pynput
from pynput.keyboard import Key, Controller, KeyCode

keyboard = Controller()

# Delay before starting to type (in seconds).
# To give you enough time to click over to the correct window.
delay = 5

# The amount of delay between each character (in seconds).
speed = .5


with open('code.txt', 'r') as file:
    my_string = file.readlines()
    

def retype(my_string):
    for line in my_string:
        print(line)
        for char in line:
            keyboard.type(char)
            time.sleep(speed)


print('Script will begin typing in:')
while delay > 0:
    print(f'{delay} seconds remaining...')
    time.sleep(1)
    delay = delay - 1

print('Begin Re-Typing...')
start = time.time()
retype(my_string)
end = time.time()
duration = end - start
print('Re-Typing COMPLETE!')
print(f'Duration: {duration} seconds.')




