# Sharp AQUOS Remote Python

Python module for sending Remote Control Codes to your Sharp AQUOS Smart TV

## IP Setup

1. Go to MENU
2. Go to the Inital Setup Tab
3. Go to Network Setup
4. Manual Setup (Click Yes)
5. Go down to IP Setup

## Remote Setup

1. Go to MENU
2. Go to the Inital Setup Tab
3. Go to AQUOS Remote Control
4. Enable AQUOS Remote 

## Usage

** Import the module

'''
	import aqous
'''

** Set IP

'''
	aquos.set_ip('xxx.xxx.xxx.xxx')
'''

** Set Login Info (If applicable)

'''
	aquos.set_login('username','password')
'''

** TV Commands

'''
	aquos.tv_on() # Will only work if you last turned off your tv with the aquos.tv_off() function 
	
	aquos.tv_off() # Puts TV into standby mode
	
	aquos.set_tv_input(x) # Sets TV input to input x
	
	aquos.set_tv_volume(xx) # Sets TV volume 0-100
	
	aquos.mute_toggle() # Toggles mute
	
	aquos.mute_on() # Turns mute on
	
	aquos.mute_off() # Turns mute off
'''

### Customize AQOUS.py

When using aquos you can either manualully adjust the values in aquos.py or you can set them using the functions 

## DEPENDENCIES

This has been tested with Python 2.6 and 2.7.

## LICENSE

MIT License