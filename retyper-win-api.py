

# python3 -m pip install pywin32
import win32com.client

import time

shell = win32com.client.Dispatch("WScript.Shell")

# Delay before starting to type (in seconds).
# To give you enough time to click over to the correct window.
delay = 5

# The amount of delay between each character (in seconds).
speed = .5

# File you want to re-type (same directory as this script).
with open('code.txt', 'r') as file:
    lines = file.readlines()
    

def retype(lines):
    for line in lines:
        print(line)
        new_line = ''
        for char in line:
            # Escape the 'SendKeys' special characters by enclosing them in '{}'
            if char == '+' or '^' or '%' or '~' or '(' or ')' or '[' or ']' or '{' or '}':
                new_line = new_line + '{' + str(char) + '}'
            else:
                new_line = new_line + str(char)
        
        shell.SendKeys(new_line)
        # Depending on the receiving application, you may need to uncomment this:
        #shell.SendKeys('{ENTER}')
        time.sleep(speed)


print('Script will begin typing in:')
while delay > 0:
    print(f'{delay} seconds remaining...')
    time.sleep(1)
    delay = delay - 1

print('Begin Re-Typing...')
start = time.time()
retype(lines)
end = time.time()
duration = end - start
print('Re-Typing COMPLETE!')
print(f'Duration: {duration} seconds.')
