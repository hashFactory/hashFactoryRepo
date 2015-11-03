import time
from sys import stdout as o
 
ticks = time.time()
while True:
    startOfGame = (time.time() - ticks)
    coins = startOfGame * 1.25
    o.write(str(round(coins, 4)) + chr(8) * 60)
    o.flush()
    time.sleep(0.016)
