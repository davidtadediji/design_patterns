from abc import ABC, abstractmethod

class EuropeanSocket(ABC):

    @abstractmethod
    def plug_in(self):
        pass


class USASocket:
    @staticmethod
    def provide_power():
        return "110v power"


class SocketAdapter(EuropeanSocket):

    def __init__(self, usa_socket: USASocket):
        self.usa_socket = usa_socket

    def plug_in(self):
        return self.usa_socket.provide_power()


socket = USASocket()
socket_adapter = SocketAdapter(socket)
print(socket_adapter.plug_in())
