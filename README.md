# Sharp AQUOS Remote Python

Python module for sending Remote Control Codes to your Sharp AQUOS Smart TV

## Install

```bash
pip install aquosRemote
```

## Setup

### Enabled AQUOS Remote Control

1. Go to MENU
2. Go to the Inital Setup Tab
3. Go to AQUOS Remote Control
4. Enable AQUOS Remote

### Find your IP

1. Go to MENU
2. Go to the Inital Setup Tab
3. Go to Network Setup
4. Manual Setup (Click Yes)
5. Go down to IP Setup

## Usage

```python
# Import Client
from aquosRemote.aquos import AquosTV

# Connect
aquos = AquosTV('IP_ADDRESS')

aquos.on() # Turns on TV

aquos.off() # Puts TV into standby mode

aqous.set_standbymode() # Enables standby mode

aquos.toggle_power() # Toggle power

aquos.toggle_power_source() # Toggle power source

aqous.delay() # Waits a certian time

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

aqous.enter() # Enter button

aqous.remote_return() # Stop button

aqous.exit() # Exit button

aqous.volume_up() # Turns volume up

aqous.volume_down() # Turns volume down

aquos.volume_repeat(x) # Turns volume up x times up or down

aquos.set_volume(xx) # Sets TV volume 0-100

aquos.toggle_mute() # Toggles mute

aqous.set_mute(boolean) # Sets mute to boolean

aquos.mute_on() # Turns mute on

aquos.mute_off() # Turns mute off

aquos.set_input(x) # Sets TV input to input x

aquos.toggle_3d() # Toggles 3D

aquos.netflix() # Opens Netflix

aquos.smart_central() # Opens Smart Central

aquos.get_device_name() # Gets TV device name

aquos.get_model_name() # Gets TV model name

aquos.get_software_version() # Gets TV software version

aquos.get_ip_protocol_version() # Gets TV ip protocol

aquos.get_info() # Returns all above info into a pretty string
```

Note: `aquos.on()` function will work only after you use the setup=True argument or after you turn off tv using this function, then un-plug and re-plug-in the tv.

## License

[![License](https://img.shields.io/pypi/l/aquosRemote?style=flat-square)](https://github.com/thehappydinoa/aquosRemote/blob/master/LICENSE)
