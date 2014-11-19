#first launch minecraft manually
import random

from mcpi import minecraft
from threading import Event, Thread, Timer
mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.player.setPos(0,y,z)

xpos = 0

# Recursively set block
def setblock():
	global xpos
	#mc.postToChat("adding block")
	x, y, z = mc.player.getPos()
	#mc.postToChat("I am at x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))
	mc.setBlock(x+1, y, z, 67)
	mc.player.setPos(x+1,y+1,z)
	#if(x < xpos-4):
	#	xpos = xpos + 2
	#	mc.player.setPos(xpos,y+1,z)
	
## METHOD TO RUN AT INTERVALS (NODE STYLE)
def call_repeatedly(interval, func, *args): ## you can pass arguments too which is useful
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set
    
def randomteleport():
	mc.player.setPos(random.randint(-20,20),random.randint(40,70),random.randint(-20,20))


randomteleport()
setblock_timer = call_repeatedly(2, setblock) #seconds
setteleport_timer = call_repeatedly(60, randomteleport) #seconds
