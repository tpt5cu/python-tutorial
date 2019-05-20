import time

start = time.time()
while(True):
    now = time.time()
    if (now > start + 3):
        print("done")
        break