import r2r_adc as r2r
import adc_plot as pl
import time

adc = r2r.R2R_ADC(3.215, 0.0001)
voltage_values = []
time_values = []
duration = 10.0
max_voltage = 3.3
try:
    t = time.time()
    while(time.time()-t <= duration):
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time.time()-t)
    pl.plot_voltage_vs_time(time_values, voltage_values, max_voltage)
    pl.plot_sampling_hist(time_values)
finally:
    adc.deinit()


