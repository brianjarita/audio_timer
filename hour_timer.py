import os
import sys
import time

def show(s):
    print(f"{s}", end="")
    sys.stdout.flush()


mins = 0
start = time.time()
while mins < 61:
    for tick in range(5):
        show(".")
        time.sleep(10)

        # Account for time spent playing the mp3
        elapsed = round(now - start)
        desired = mins * 60 + tick * 10
        if (desired - elapsed) < 1:
            continue
        time.sleep(round(desired-elapsed))

    show("m")
    mins += 1
    if mins % 5 == 0:
        cmd = f"afplay {mins}mins.mp3"
        print(f"\n{cmd}")
        os.system(cmd)
