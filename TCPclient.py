import socket

class Connection():

    ip_address = property()
    port_number = property()

# get и set ip-адреса
    @ip_address.getter
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        self.__ip_address = ip_address

# get и set номера порта
    @port_number.getter
    def port_number(self):
        return self.__port_number

    @port_number.setter
    def port_number(self, port_number):
        self.__port_number = port_number

    def begin_connection(self, ip_address, port_number):
        self.sock = socket.socket()
        self.__ip_address = ip_address
        self.__port_number = port_number
        try:
            self.sock.connect((ip_address, port_number))
            self.sock.timeout = 5
        except AttributeError:
            return 1
        except TimeoutError:
            return 2
        except Exception:
            return 3
        else:
            return 0

    def send_message(self, message_byte):
        try:
            self.sock.send(message_byte)
        except AttributeError:
            return 1
        except Exception:
            return 2
        else:
            return 0

    def close_connection(self):
        try:
            self.sock.close()
        except AttributeError:
            return 1
        else:
            return 0

    def data_read(self):
        try:
            data = self.sock.recv(1024)
            print(type(data))
        except TimeoutError:
            return 1
        except Exception:
            return 2
        else:
            return data

