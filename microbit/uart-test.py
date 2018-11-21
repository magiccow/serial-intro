from microbit import *

uart.init(baudrate=9600,tx=pin8,rx=pin12)
greet = 'AAA'
display.scroll('Online '+greet)

while True:
    if uart.any():
      message = uart.read()
      display.scroll(message)
    else:
      sleep(20)
    
    if button_a.is_pressed():
        uart.write(greet)
        sleep(50)