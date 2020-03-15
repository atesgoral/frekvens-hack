import time

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

gpioR.setOutputDirection()
gpioG.setOutputDirection()
gpioB.setOutputDirection()

gpioLatch.setOutputDirection()
gpioClock.setOutputDirection()
gpioData.setOutputDirection()

gpioR.setValue(1)
gpioG.setValue(1)
gpioB.setValue(1)

gpioLatch.setValue(0)
gpioClock.setValue(0)

while True:
    for y in range(0, 16):
        for x in range(0, 16):
            gpioData.setValue(y & x & 1)

            gpioClock.setValue(1)
            time.sleep(1.0 / 1000)
            gpioClock.setValue(0)
            time.sleep(1.0 / 1000)

    gpioLatch.setValue(1)
    time.sleep(1.0 / 1000)
    gpioLatch.setValue(0)
    time.sleep(1.0 / 1000)

    time.sleep(10.0 / 1000)
