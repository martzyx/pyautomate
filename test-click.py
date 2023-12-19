import pyautogui
import time

repeated_sequence = [
    (678.98046875, 551.78125), # open collapsible design
    (426.55859375, 673.28515625), # select options
    (502.265625, 689.33203125), # rec design
    (1354.73046875, 283.08984375), # save
    # (268.578125, 280.796875) # back
]

last_repeat = [
    (678.98046875, 551.78125), # open collapsible design
    (426.55859375, 673.28515625), # select options
    (473.8125, 714.78125), # blog design
    (1354.73046875, 283.08984375), # save
    # (268.578125, 280.796875) # back
]

coordinates = [
    (1353, 434.81640625),  # first content
    "repeat",
    (1353, 463.375),  # next content
    "repeat",
    (1353, 503),  # so on
    "repeat",
    (1353, 537.0),
    "repeat",
    (1353, 571.20703125),
    "repeat",
    (1353, 615.2421875),
    "repeat",
    (1353, 651.87109375),
    "repeat",
    (1353, 685.578125),
    "repeat",
    (1353, 712.07421875),
    "repeat",
    (1353, 748.40625),
    "repeat",
    (1353, 796.42578125),
    "repeat",
    (1353, 830.0390625), # last content needs to be different
    "last_repeat"

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
    else:
        x, y = coord
        time.sleep(0.4)  # after saving
        pyautogui.click(x, y)
        time.sleep(0.4)  # after edit
