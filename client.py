import time
# import atexit

import onionGpio

pinR = 17
pinG = 16
pinB = 15

pinLatch = 18
pinClock = 19
pinData = 20

gpioR = onionGpio.OnionGpio(pinR)
gpioG = onionGpio.OnionGpio(pinG)
gpioB = onionGpio.OnionGpio(pinB)

gpioLatch = onionGpio.OnionGpio(pinLatch)
gpioClock = onionGpio.OnionGpio(pinClock)
gpioData = onionGpio.OnionGpio(pinData)

# def exit_handler():
    # gpioR._freeGpio()
    # gpioG._freeGpio()
    # gpioB._freeGpio()
    # gpioLatch._freeGpio()
    # gpioClock._freeGpio()
    # gpioData._freeGpio()

# atexit.register(exit_handler)

gpioR.setOutputDirection(1)
gpioG.setOutputDirection(1)
gpioB.setOutputDirection(1)

gpioLatch.setOutputDirection(0)
gpioClock.setOutputDirection(0)
gpioData.setOutputDirection(0)

f = 0

while True:
    for y in range(0, 16):
        for x in range(0, 16):
            gpioData.setValue(x & y & 1)

            gpioClock.setValue(1)
            time.sleep(1.0 / 1000)
            gpioClock.setValue(0)
            time.sleep(1.0 / 1000)

    gpioLatch.setValue(1)
    time.sleep(1.0 / 1000)
    gpioLatch.setValue(0)
    time.sleep(1.0 / 1000)

    f = f + 1

    gpioR.setValue(f & 1)
    gpioG.setValue(f >> 1 & 1)
    gpioB.setValue(f >> 2 & 1)

    time.sleep(10.0 / 1000)
