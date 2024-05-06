import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

callibirated = False

hx = HX711(dout_pin=6, pd_sck_pin=5)
hx.zero()

input("Place Known Weight on Scale & Press Enter")

reading = hx.get_data_mean(readings=100)
print(reading)
known_weight_grams = input('Enter Weight of Placed Object in grams: ')
value = float(known_weight_grams)

ratio = reading/value
print(ratio)
hx.set_scale_ratio(ratio)
callibirated = True

while True:
    weight = hx.get_weight_mean()
    a = int(weight)
    if a < 0:
        print("weight: 0")
    else:
        print("Weight: ", a)
    


