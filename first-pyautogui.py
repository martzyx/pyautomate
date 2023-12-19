from pynput import mouse, keyboard

x_pressed = False

def on_click(x, y, button, pressed):
    global x_pressed
    if pressed and button == mouse.Button.left and x_pressed:
        print(f"({x}, {y})")

def on_press(key):
    global x_pressed
    try:
        if key.char == 'x':  # Check if the key is 'x'
            x_pressed = True
    except AttributeError:
        pass

def on_release(key):
    global x_pressed
    try:
        if key.char == 'x':
            x_pressed = False
    except AttributeError:
        pass

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()
