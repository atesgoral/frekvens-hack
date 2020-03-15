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

gpioR.setValue(0)
gpioG.setValue(1)
gpioB.setValue(0)
