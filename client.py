import onionGpio

pinR = 17
pinG = 16
pinB = 15

gpioR = onionGpio.OnionGpio(pinR)
gpioG = onionGpio.OnionGpio(pinG)
gpioB = onionGpio.OnionGpio(pinB)

gpioR.setOutputDirection()
gpioG.setOutputDirection()
gpioB.setOutputDirection()

gpioR.setValue(0)
gpioG.setValue(1)
gpioB.setValue(0)
