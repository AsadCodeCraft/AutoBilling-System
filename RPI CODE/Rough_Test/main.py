import cv2
import os
import sys, getopt
import signal
import time
from edge_impulse_linux.image import ImageImpulseRunner

import RPi.GPIO as GPIO 
from hx711 import HX711

import requests
import json
from requests.structures import CaseInsensitiveDict

runner = None
show_camera = True

flag = 0

global id_product
id_product = 1
list_label = []
count = 0
taken = 0

t = 'Apple'
b = 'Banana'

def now():
    return round(time.time() * 1000)

def post(label,price,final_rate,taken):
    global id
    url = "https://autu-billing-test.onrender.com/product/"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data_dict = {"id":id_product,"name":label,"price":price,"units":"units","taken":taken,"payable":final_rate}
    data = json.dumps(data_dict)
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    id_product = id_product + 1  
    time.sleep(1)
    list_label = []
    list_weight = []
    count = 0
    final_weight = 0
    taken = 0

def rate(final_weight,label,taken):
    print("Calculating rate")
    if label == a :
         print("Calculating rate of",label)
         final_rate_a = final_weight * 0.01
         price = 10     
         post(label,price,final_rate_a,taken)
    elif label ==b :
         print("Calculating rate of",label)
         final_rate_b = final_weight * 0.02
         price = 20
         post(label,price,final_rate_b,taken)
    elif label == l:
         print("Calculating rate of",label)
         final_rate_l = 1
         price = 1
         post(label,price,final_rate_l,taken)
    else :
         print("Calculating rate of",label)
         final_rate_c = 2
         price = 2
         post(label,price,final_rate_c,taken)

def get_webcams():
    for i in range(-1, 10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            port = cap.get(cv2.CAP_PROP_POS_MSEC)
            print("Connected to camera port {}".format(port))
            cap.release()
            return port
            break
        else:
            cap.release()
        if not cap.isOpened():
            print("Failed to connect to any camera")
            

def main():
    modelfile = "./modelfile.eim"
    print('MODEL: ' + modelfile)


if __name__ == "__main__":
    main()


