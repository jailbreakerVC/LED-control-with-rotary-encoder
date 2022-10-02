
import time
import board
import neopixel
import digitalio


pixel_pin = board.GP28
num_pixels = 30

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

WHITE=(255,255,255)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
COLORS=[RED,YELLOW,GREEN,CYAN,BLUE,PURPLE]
number=0


#Pico
dirPin = digitalio.DigitalInOut(board.GP16)
stepPin = digitalio.DigitalInOut(board.GP17)
dirPin.direction = digitalio.Direction.INPUT
stepPin.direction=digitalio.Direction.INPUT

dirPin.pull=digitalio.Pull.UP
stepPin.pull=digitalio.Pull.UP
previousvalue=True
print(stepPin.value)
while True:
   
    
    if number==1:
        pixels.fill(WHITE)
        pixels.show()
    elif number==2:
        pixels.fill(CYAN)
        pixels.show()
    elif number==3:

        pixels.fill(RED)
        pixels.show()
    elif number==-2:

        pixels.fill(BLUE)
        pixels.show()
    elif number==-4:
        pixels.fill(PURPLE)
        pixels.show()
    elif number==-6:
        pixels.fill(YELLOW)
        pixels.show()
    elif number==50:
        print("damn")
    if previousvalue != stepPin.value:
        if stepPin.value==False:
            if dirPin.value==False:
                #print("TO THE LEFT")
                number=number-1
                print(number)
            elif dirPin.value==True:
                #print("to the right")
                
                number+=1
                print(number)
                

        previousvalue=stepPin.value



