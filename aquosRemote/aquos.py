import socket
from contextlib import closing


class aquosTV(object):
    def __init__(self, ip, port=10002, username=None, password=None):
        self.ip = str(ip)
        self.port = int(port)
        self.username = username
        self.password = password
        if not self._check_ip():
            raise Exception("Port %s is not open on %s" % (self.port, self.ip))

    def send_command(self, command, byte_size=1024, timeout=3):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            s.settimeout(timeout)
            if (self.username and self.password):
                s.send(self.username + "\r" + self.password + "\r")
            s.send(command.encode('utf-8'))
            msg = s.recv(byte_size)
            return msg
        except socket.error:
            raise Exception("Error connecting to %s:%s" %
                            (self.ip, self.port))

    def off(self):
        return self.send_command("POWR0   \r")

    def set_standbymode(self):
        return self.send_command("RSPW1   \r\r")

    def on(self):
        return self.send_command("POWR1   \r")

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
        return self.send_command("MUTE0   \r")

    def mute_on(self):
        return self.send_command("MUTE1   \r")

    def mute_off(self):
        return self.send_command("MUTE2   \r")

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
            return "error"
        return "OK\r"

    def set_volume(self, level):
        if level > 9:
            sLevel = str(level) + "  "
        elif level <= 9:
            sLevel = str(level) + "   "
        elif level == 100:
            sLevel = str(level) + " "

        if (level <= 100 and level >= 0):
            return self.send_command("VOLM" + sLevel + "\r")
        return "error"

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
        return self.send_command("IAVD" + str(input_name) + "   \r")

    def toggle_input(self):
        return self.send_command("ITGD   \r")

    def remote_number(self, number):
        if number > 9:
            number = str(number) + "  "
        else:
            number = str(number) + "   "
        return self.send_command("RCKY" + number + "\r")

    def _check_ip(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(3)
            return (sock.connect_ex((self.ip, self.port)) == 0)


if __name__ == "__main__":
    # Example
    # aquos = aquosTV("Basement TV", "192.168.1.2")
    from time import sleep
    aquos = aquosTV("192.168.1.2")
    aquos.on()
    sleep(1)
    aquos.set_volume(30)
    sleep(1)
    aquos.off()
