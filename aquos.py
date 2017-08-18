''' 
|  @file aquos.py
|  @brief A Small module for interactions with any Sharp AQOUS TVs
|  
'''

import socket, logging, time, sys

#logging.basicConfig(level=logging.DEBUG)


tv_ip = ''
login = False
username = ''
password = ''

def send_command(command):
	if (tv_ip == ''):
		raise Exception('No IP set. Please set using set_ip(ip) to set ip.')
	else:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((tv_ip, 10002))
			if (login):
				s.send(username +"\r" + password +"\r")
				logging.debug(s.recv(1024))
			s.send(command)
			msg = s.recv(1024)
			return msg
		except Exception, e:
			return "error"
	
def off():
	return send_command("POWR0   \r")
	
def set_standbymode():
	return send_command("RSPW2   \r\r")

def on():
	return send_command("POWR1   \r")
	
def play():
	return remote_number(16)
	
def pause():
	return remote_number(16)
	
def stop():
	return remote_number(20)
	
def rewind():
	return remote_number(15)
	
def fast_forward():
	return remote_number(17)
	
def skip_forward():
	return remote_number(21)
	
def skip_back():
	return remote_number(19)

def toggle_mute():
	return send_command("MUTE0   \r")

def mute_on():
	return send_command("MUTE1   \r")

def mute_off():
	return send_command("MUTE2   \r")
	
def volume_up():
	return remote_number(33)
	
def volume_down():
	return remote_number(32)

def set_tv_volume(level):
	if (level <= 100 and level >= 0):
		return send_command("VOLM" + level + "   \r")
	return "error"
	
def up():
	return remote_number(41)
	
def right():
	return remote_number(44)
	
def down():
	return remote_number(42)
	
def left():
	return remote_number(43)
	
def favorite_app(number):
	if number == 1:
		return remote_number(55)
	elif number == 2:
		return remote_number(56)
	elif number == 2:
		return remote_number(57)
		
def netflix():
	return remote_number(59)
		
def set_tv_input(input):
	return send_command("IAVD" + input + "   \r")
	
def toggle_input():
	return send_command("ITGD   \r")
	
def remote_number(number):
	return send_command("RCKY" + number + "   \r"
	
def 
	
def set_login(user,passwd):
	global username, password
	if not login:
		login = True
		username = str(user)
		password = str(passwd)
	return True
	
def set_ip(ip):
	global tv_ip
	tv_ip = str(ip)
	return True
	
		
if __name__ == "__main__":		
	
	# Example
	aquos.set_ip('192.168.1.12')
	'''
	Enter username and password if it applies to you
	aquos.set_login(username,password)
	'''
	aquos.tv_on()
	aquos.set_tv_volume(30)
	
	