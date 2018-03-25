from functools import partial
from gpiozero import Button, RGBLED, Device
from signal import pause
from sound_manager import SoundManager
from time import sleep
import asyncio


GPIO_PLAY = Button(21)
RGB_LED = RGBLED(17,18,27)

def play_story(sound_manager):
    print("[PLAY EVENT]")
    sound_manager.nextRandomSong()

def stop(sound_manager):
    print("stop")


def volume_down(sound_manager):
    print("softer")


presses = {
    GPIO_PLAY: play_story,
}

holds = {
    GPIO_PLAY: stop,
}
    

async def buttons(mySoundManager):
    while True:
        for button, event in presses.items():
            print("[BUTTONS] REGISTER")
            button.when_pressed = partial(event, mySoundManager)
            await asyncio.sleep(1)
        await asyncio.sleep(10000)

async def leds(mySoundManager):
    prevState = True

    while True:
        try: 
            print("[LED] status is %s" % mySoundManager.isStatePlay() )
            if(mySoundManager.isStatePlay() and prevState != True): 
                RGB_LED.blink( on_color=(1, 1, 0.2), off_color=(1, 0.2, 1), fade_in_time=2, fade_out_time=2, )
            elif(mySoundManager.isStatePlay() == False and prevState != False): 
                print("[LED] currently not playing led is green")
                RGB_LED.blink( on_color=(1, 1, 0), off_color=(1, 0.1, 0), fade_in_time=2, fade_out_time=2, )
            prevState = mySoundManager.isStatePlay();
            await asyncio.sleep(1)
        except:
            print ("[LED] This ain't good but it will restart it self after 2sec")
            await asyncio.sleep(2)


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


    # RGB_LED.blink( on_color=(0, 0, .1), off_color=(1, 0, 0), fade_in_time=2, fade_out_time=2, )




    print("[MAIN] creating soundmanager")
    mySoundManager = SoundManager()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        leds(mySoundManager),
        buttons(mySoundManager),
    ))
    loop.close()

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
