# then launch from SSH as 'sudo python minecraftbot.py'
import os
from mcpi import minecraft

## Sadly this hack to launch minecraft via SSH didn't work. 
#os.system("echo 'hello world'")
#os.system("minecraft-pi")  

## So we have to use a program like Remoter to look at the rPi screen remotely and click to launch Minecraft

## now we can initiate our python - minecraft session
mc = minecraft.Minecraft.create()
mc.postToChat("Hello world")


## for more try these links:
# http://www.raspberrypi.org/documentation/usage/minecraft/
# http://www.stuffaboutcode.com/p/minecraft.html
