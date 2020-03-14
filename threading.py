#!/usr/bin/env python3

# Simple threading demo / starter template

import threading
import time
import sys

class Timer():
    def __init__(self):
        pass

    def run(self):
        while True:
            print("Timed operation 1")
            time.sleep(5)
            print("Timed operation 2")
            time.sleep(5)
            print("Timed operation 3")
            time.sleep(5)


class Demo():

    def __init__(self):
        pass

    def run(self):
        while True:
            print("Hello from Demo!")
            time.sleep(1)



def timerService():
    t=Timer()
    t.run()

def demoService():
    d=Demo()
    d.run()

if __name__=="__main__":
    timerservice_th=threading.Thread(target=timerService, daemon=True)
    demoservice_th=threading.Thread(target=demoService, daemon=True)

    timerservice_th.start()
    demoservice_th.start()

    try:
        while True:
            time.sleep(30)
            print("Healthcheck")
    except KeyboardInterrupt:
        sys.exit(0)