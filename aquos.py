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
	
def tv_off():
	return send_command("RSPW2   \r\rPOWR0   \r")

def tv_on():
	return send_command("POWR1   \r")

def mute_toggle():
	return send_command("MUTE0   \r")

def mute_on():
	return send_command("MUTE1   \r")

def mute_off():
	return send_command("MUTE2   \r")

def set_tv_volume(level):
	if (level <= 100 and level >= 0):
		return send_command("VOLM" + level + "   \r")
	return "error"

def set_tv_input(input):
	return send_command("IAVD" + input + "   \r")
	
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
	
	