from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print(f"({x}, {y})")

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
