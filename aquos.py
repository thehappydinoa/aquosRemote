''' 
|  @file aquos.py
|  @brief A Small module for interactions with any Sharp AQOUS TVs
|  
'''

import socket, logging, time

logging.basicConfig(level=logging.DEBUG)

class aquos():
	
	tv_ip = ''
	login = False
	username = ''
	password = ''
	
	def send_command(command):
		if (tv_ip == ''):
			logging.critical("Critical exception: No IP set")
			break
		else:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((tv_ip, 10002))
				if (login):
					s.send(username +"\r" + password +"\r")
					logging.debug(s.recv(1024))
				s.send(command)
				logging.debug(s.recv(1024))
				return True
			except Exception, e:
				logging.critical("Critical exception: " + str(e))
				break
		
	def tv_off():
		send_command("RSPW2   \r\rPOWR0   \r")
		return True

	def tv_on():
		send_command("POWR1   \r")
		return True

	def mute_toggle():
		send_command("MUTE0   \r")
		return True
	
	def mute_on():
		send_command("MUTE1   \r")
		return True
	
	def mute_off():
		send_command("MUTE2   \r")
		return True
	
	def set_tv_volume(level):
		if (level <= 100 and level >= 0)
			send_command("VOLM" + level + "   \r")
		return True

	def set_tv_input(input):
		send_command("IAVD" + input + "   \r")
		return True
		
	def set_login(user,passwd)
		if not login:
			login = True
			username = str(user)
			password = str(passwd)
		return True
		
	def set_ip(ip)
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
	
	