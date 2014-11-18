botcaves
========
A collection of bot scripts to run from a Raspberry Pi.

Installation Notes
==================================
1. For this workshop we are using rPis (B and B+) with WIFI dongles. 
2. The OS we've installed is Raspbian (on 8Gb SD’s for the Raspberry Pi B and 16Gb SDxC for the Raspberry Pi B+)
3. The OS and WIFI setup is covered here: http://www.iiclouds.org/20141117/basic-instructions-to-set-up-a-raspberry-pi/
4. Once you have the Pi connected to the WIFI and know its IP address you can connect to it from another computer with SSH
5. In terminal on your main computer type ssh pi@xxx.xxx.x.xxx, you'll be asked to enter the Pi's password

*you're in!*

6. Install some software on the pi. The following are terminal commands for upgrading python, installing pip and then tywthon
7. sudo apt-get install python dev
8. sudo apt-get install python-pip
9. sudo pip install twython

*you have python and libraries!*

10. Set up a new profile on twitter. Open an account, go to dev.twitter.com to create an app and get API keys. 
11. Download the twitterbot-example.py script and change it to have your new API keys.
12. Open a new terminal window. We will use this to copy/paste over the twitterbot-example.py file
13. scp /Users/myname/Desktop/botexample.py pi@XX.XXX.XXX.XXX/usr/local/bin

*your bot script in on the Pi!*

14. The script will be in the Pis HOME directory. You may want to move it somewhere else such as /usr/local/bin/
15. In your SSH terminal session go to  HOME directory. Run the script with this line of code:
16. python twitterbot-example.py

*the bot is running!*

17. To keep the bot running when you close SSH you may want to start it differently. The options are:
18. install 'screen' (sudo apt-get install screen) then is SSH start the screen mode (screen) then run the bot
19. Run with an ampersand (&) to keep script running 'headless' (python twitterbot-example.py &) *method not tested
20. Set up either a cron timer or init launch deamon *method not tested
