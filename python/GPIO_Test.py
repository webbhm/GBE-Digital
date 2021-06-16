from RPIO import PWM

PWM.setup()
PWM.init_channel(4)

PWM.add_Channel_pulse(4, 21, 0, 50)
PWM.add_Channel_pulse(4, 21, 100, 50)

PWM.clear_channel_gpio(0, 17)
PWM.cleanup()

