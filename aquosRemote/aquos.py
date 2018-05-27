import socket
from time import sleep
from contextlib import closing


class aquosTV(object):
    def __init__(self, ip, port=10002, username=None, password=None, setup=False):
        self.ip = str(ip)
        self.port = int(port)
        self.auth = (username and password)
        self.username = username
        self.password = password
        if not self._check_ip():
            if setup:
                self.on()
                sleep(1)
                self.set_standbymode()
                self.off()
            raise Exception("Port %s is not open on %s" % (self.port, self.ip))

    def _check_ip(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(3)
            return (sock.connect_ex((self.ip, self.port)) == 0)

    def format_command(self, command):
        if not command.endswith("\r"):
            new_command = command
            number = command[4:]
            if number.isdigit():
                new_command = command[:4] + self.format_number(number)
            new_command += "\r"
            return new_command
        return command

    def format_number(self, number):
        return "% 4d" % int(number)

    def send_command(self, command, byte_size=1024, timeout=3):
        command = self.format_command(command)
        # print(command)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            s.settimeout(timeout)
            if (self.auth):
                s.send(self.username + "\r" + self.password + "\r")
            s.send(command.encode('utf-8'))
            msg = s.recv(byte_size)
            return msg.strip()
        except socket.error:
            raise Exception("Error connecting to %s:%s" %
                            (self.ip, self.port))

    def remote_number(self, number):
        number = self.format_number(number)
        return self.send_command("RCKY" + number)

    def off(self):
        return self.send_command("POWR0")

    def set_standbymode(self, mode=1):
        return self.send_command("RSPW" + self.format_number(mode))

    def on(self):
        return self.send_command("POWR1")

    def play(self):
        return self.remote_number(16)

    def pause(self):
        return self.remote_number(16)

    def stop(self):
        return self.remote_number(20)

    def rewind(self):
        return self.remote_number(15)

    def fast_forward(self):
        return self.remote_number(17)

    def skip_forward(self):
        return self.remote_number(21)

    def skip_back(self):
        return self.remote_number(19)

    def toggle_mute(self):
        return self.send_command("MUTE0")

    def mute_on(self):
        return self.send_command("MUTE1")

    def mute_off(self):
        return self.send_command("MUTE2")

    def volume_up(self):
        return self.remote_number(33)

    def volume_down(self):
        return self.remote_number(32)

    def volume_repeat(self, number):
        x = 0
        if number < 0:
            while x > number:
                self.volume_down()
                x -= 1
        elif number > 0:
            while x < number:
                self.volume_up()
                x += 1
        else:
            return "ERR"
        return "OK"

    def set_volume(self, level):
        if (level <= 60 and level >= 0):
            level = self.format_number(level)
            return self.send_command("VOLM" + level)
        return "ERR"

    def up(self):
        return self.remote_number(41)

    def right(self):
        return self.remote_number(44)

    def down(self):
        return self.remote_number(42)

    def left(self):
        return self.remote_number(43)

    def favorite_app(self, number):
        if number == 1:
            return self.remote_number(55)
        elif number == 2:
            return self.remote_number(56)
        elif number == 2:
            return self.remote_number(57)

    def netflix(self):
        return self.remote_number(59)

    def set_input(self, input_name):
        return self.send_command("IAVD" + str(input_name))

    def toggle_input(self):
        return self.send_command("ITGD1")

    def get_device_name(self):
        return self.send_command("TVNM1")

    def get_model_name(self):
        return self.send_command("MNRD1")

    def get_software_version(self):
        return self.send_command("SWVN1")

    def get_ip_protocol_version(self):
        return self.send_command("IPPV1")


if __name__ == "__main__":
    # Example
    # aquos = aquosTV("192.168.1.2")
    aquos = aquosTV("192.168.1.2", setup=True)
    aquos.on()
    sleep(1)
    # print(aquos.get_device_name())
    # print(aquos.get_model_name())
    # print(aquos.get_software_version())
    # print(aquos.get_ip_protocol_version())
    aquos.set_volume(30)
    sleep(1)
    aquos.off()
