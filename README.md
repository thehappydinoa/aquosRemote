# Sharp AQUOS Remote Python 📺

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

* Import the module

```python
import aqous
```
* Set IP

```python
aquos.set_ip('xxx.xxx.xxx.xxx')
```

* Set Login Info (If applicable)

```python
aquos.set_login('username','password')
```

* TV Commands

```python
aquos.on() # Turns on TV 
	
aquos.off() # Puts TV into standby mode

aqous.set_standbymode # Enables standby mode

aquos.play() # Play button (⏯)

aquos.pause() # Pause button (⏯)

aqous.stop() # Stop button

aquos.rewind() # Rewind button (⏪)

aqous.fast_forward() # Fast forward button (⏩)

aquos.rewind() # Skip forward button (⏭)

aquos.rewind() # Skip back button (⏮)

aqous.up() # Up button (▲)

aqous.down() # Down button (▼)

aqous.left() # Left button (◄)

aqous.right() # Right button (►)

aqous.volume_up() # Turns volume up

aqous.volume_down() # Turns volume down

aquos.volume_repear(x) # Turns volume up x times up or down 
	
aquos.set_volume(xx) # Sets TV volume 0-100
	
aquos.toggle_mute() # Toggles mute
	
aquos.mute_on() # Turns mute on
	
aquos.mute_off() # Turns mute off

aquos.set_input(x) # Sets TV input to input x
```
Note: tv_on function will work only after you turn off tv using this function, then un-plug and re-plug-in the tv.

## Example

An example program would look like:

```python
import aquos

aquos.set_ip('IP.ADD.RESS.XX')
aquos.set_login('username','password')
aquos.tv_on()
...
```

## DEPENDENCIES

This has been tested with Python 2.6 and 2.7.

## LICENSE

MIT License
