#first launch minecraft manually

from mcpi import minecraft
from threading import Event, Thread, Timer
mc = minecraft.Minecraft.create()


# Recursively set block
def setblock():
	mc.postToChat("adding block")
	x, y, z = mc.player.getPos()
	mc.setBlock(x+1, y, z, 1)
	mc.player.setPos(x-1,y,z)
	
## METHOD TO RUN AT INTERVALS (NODE STYLE)
def call_repeatedly(interval, func, *args): ## you can pass arguments too which is useful
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set
    

setblock_timer = call_repeatedly(5, setblock) #seconds

## for more try these links:
# http://www.stuffaboutcode.com/2013/01/raspberry-pi-minecraft-api-basics.html
# http://www.raspberrypi.org/documentation/usage/minecraft/
# http://www.stuffaboutcode.com/p/minecraft.html
