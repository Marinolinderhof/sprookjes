from gpiozero import Button
from signal import pause

GPIO_PLAY = Button(3, held_time=2)
GPIO_UP = Button(5)
GPIO_DOWN = Button(7)


def play_story():
    print("tell a story")


def stop():
    print("stop")


def volume_up():
    print("louder")


def volume_down():
    print("softer")


presses = {
    GPIO_PLAY: play_story,
    GPIO_UP: volume_up,
    GPIO_DOWN: volume_down,
}

holds = {
    GPIO_PLAY: stop,
}


def wait_for_events():
    print("starting")
    while True:
        for button, event in presses.items():
            button.when_pressed = event
        for button, event in holds.items():
            button.when_held = event
        pause()

if __name__ == "__main__":
    wait_for_events()
