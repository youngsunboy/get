import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]

        self.comp_gpio = 21
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(elem) for elem in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for i in range(255):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) or i==255:
                return i*self.dynamic_range/255

    def get_sc_voltage(self):
        volt = self.sequential_counting_adc()
        print(f"VOLTAGE: {volt}\n")
        return volt
    def successful_approximation_adc(self):
        l = 0
        r = 255
        while(l<r-1):
            m = (l+r)//2
            self.number_to_dac(m)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                r = m
            else:
                l = m
        return l

    def get_sar_voltage(self):
        volt = (self.successful_approximation_adc()/255.0)*self.dynamic_range
        print(f"VOLTAGE: {volt}\n")
        return volt


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.215)
        while True:
            #adc.get_sc_voltage()
            adc.get_sar_voltage()
    finally:
        adc.deinit()
