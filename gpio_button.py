from gpiozero import Button

GPIO_PLAY = Button(3)

GPIO_PLAY.wait_for_press()
print('You pushed me')