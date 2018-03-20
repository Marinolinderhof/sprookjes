from functools import partial
from gpiozero import Button, RGBLED, Device
from signal import pause
from sound_manager import SoundManager
from time import sleep

GPIO_PLAY = Button(21)
RGB_LED = RGBLED(17,18,27)

def play_story(sound_manager):
    print("tell a story")
    sound_manager.nextRandomSong()

def stop(sound_manager):
    print("stop")


def toggle_red_led(status=None):
    # Because of NAND ON == OFF
    if status == "on":
        LED_RED.off()
        return

    if status == "off":
        LED_RED.on()
        return
    
    LED_RED.toggle();  


def volume_down(sound_manager):
    print("softer")


presses = {
    GPIO_PLAY: play_story,
}

holds = {
    GPIO_PLAY: stop,
}


def main():
    # RGB_LED.blink( on_color=(0, 0, .1), off_color=(1, 0, 0), fade_in_time=2, fade_out_time=2, )

    # blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0, on_color=(1, 1, 1), off_color=(0, 0, 0), n=None, background=True)
    # steps
    # turn of red led and turn on yellow
    # initiate sound manager
    # green led on 
    # wait for button

    # sleep(10)
    # LED_BLUE.off()
    # LED_RED.off()

    print("[MAIN] creating soundmanager")
    mySoundManager = SoundManager()
    print("[MAIN] status soundmanager")
    print (mySoundManager.status())
    RGB_LED.blink( on_color=(0, 0, .1), off_color=(1, 0, 0), fade_in_time=2, fade_out_time=2, )

    print("[MAIN] Waiting for button press")
    while True:
        for button, event in presses.items():
            button.when_pressed = partial(event, mySoundManager)
        pause()

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
    # LED_RED.off()
    # Device.close()
    print('Destroy')

if __name__ == '__main__':
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
