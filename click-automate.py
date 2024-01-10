import pyautogui
import time

repeated_sequence = [
    (710.89453125, 514.75),
    (456.6796875, 638.49609375),
    (449.703125, 664.90234375),
]

last_repeat = [
    (769.9375, 532.54296875), # open collapsible dexxxsign
    (436.92578125, 666.6875), # select options
    (476.0234375, 683.65625), # blog design
]

save_close = [
    (1321.8203125, 274.15625), # save and close
]

coordinates = [ # requires screen to be 75% zoom
    (1311.18359375, 447.59765625),  # first content
    "repeat",
    "save_close",
    (1311.18359375, 482.64453125), # next content
    "repeat",
    "save_close",
    (1311.18359375, 516.4609375), # so on
    "repeat",
    "save_close",
    (1311.18359375, 552.2265625),
    "repeat",
    "save_close",
    (1311.18359375, 587.14453125),
    "repeat",
    "save_close",
    (1311.18359375, 621.19140625),
    "repeat",
    "save_close",
    (1311.18359375, 651.58984375),
    "repeat",
    "save_close",
    (1311.18359375, 689.53515625),
    "repeat",
    "save_close",
    (1311.18359375, 723.34765625),   
    "repeat",
    "save_close",
    (1311.18359375, 756.37890625),
    "repeat",
    "save_close",
    (1311.18359375, 791.640625),
    "repeat",
    "save_close",
    (1311.18359375, 861.3046875),
    "last_repeat", # last content needs to select blog design
    "save_close",
]

# Initial delay
time.sleep(3)

for coord in coordinates:
    if coord == "repeat":
        for x, y in repeated_sequence:
            pyautogui.click(x, y)
            time.sleep(0.1)  
    elif coord == "last_repeat":
        for x, y in last_repeat:
            pyautogui.click(x, y)
            time.sleep(0.1)  
    elif coord == "save_close":
        for x,y in save_close:
            time.sleep(0.3)  # needs sleep before clicking save
            pyautogui.click(x, y)
    else:
        x, y = coord
        time.sleep(0.3)  # after saving
        pyautogui.click(x, y)
        time.sleep(0.3)  # after edit
